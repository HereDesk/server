#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
import string
from datetime import datetime
import xlsxwriter

import operator
from functools import reduce  

from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count

from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release

from app.models import ModuleA
from app.models import ModuleB

from app.models import Authentication
from app.models import User

from app.models import BugType
from app.models import BugStatus
from app.models import BugPriority
from app.models import BugSeverity
from app.models import Bug
from app.models import BugAnnex
from app.models import BugHistory
from app.models import BugSolution
from app.models import BugReport

from app.models import TestCase
from app.models import TestSuite
from app.models import TestSuiteCell

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_user_name
from app.api.auth import get_uid
from app.api.auth import get_user_group

# get cureent time
curremt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
visualtime = time.strftime("%Y%m%d%H%M%S", time.localtime())

# 日志记录
def bug_log_record(request,userId,bug_id,status):
    req = json.loads(request.body)
    if "remark" in req:
        remark = req["remark"]
    else:
        remark = ""

    if len(remark) > 2000:
        return JsonResponse({"status":40004,"msg":"长度超出"})
        
    msg = ""
    if status == "create":
        msg = "创建了缺陷。"
        remark = ""

    if status == "close":
        msg = "关闭了缺陷。"

    if status == "Hang-up":
        msg = "将缺陷挂起"
    
    if status == "edit":
        del req["bug_id"]
        if len(req) == 1 and "priority" in req:
            msg = "修改缺陷优先级为：{0}".format(req["priority"])
        else:
            msg = "修改了缺陷"
        remark = ""
    
    try:
        log = BugHistory(
            user_id = userId,
            bug_id = bug_id,
            desc = msg,
            remark = remark
            )
    except Exception as e:
        print(e)
        pass
    else:
        log.save()


"""
 缺陷属性
"""
@require_http_methods(["GET"])
def bug_property(request):
    try:
        # bug type
        bug_type = BugType.objects.all().values("key","name")

        # bug priority
        bug_priority = BugPriority.objects.all().values("key","name")

        # bug severity
        bug_severity = BugSeverity.objects.all().values("key","name")
        
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"系统出错了"})
    else:
        return JsonResponse({
            "status":20000,
            "bug_type":list(bug_type),
            "bug_priority":list(bug_priority),
            "bug_severity":list(bug_severity)
            })

"""
  缺陷：解决方案list
"""
@require_http_methods(["GET"])
def bug_solution(request):
    try:
        data = BugSolution.objects.all().values("key","name") 
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"系统出错了"})
    else:
        return JsonResponse({"status":20000,"data":list(data)})

"""
  缺陷list
"""
@csrf_exempt
@require_http_methods(["GET"])
def bug_list(request):

    # query builder
    conditions = Q()
    q1 = Q()
    q1.connector = "AND"
    
    try:
        req = request.GET.dict()
        product_code = req["product_code"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"请求缺少必要的值"})

    if "release" in req:
        try:
            release = req["release"]
            if release == "all":
                del req["release"]
            else:
                release_query = Release.objects.filter(Q(product_code=product_code) & Q(version=release)).values('id')
                if len(release_query) == 0:
                    return JsonResponse({"status":40004,"msg":"版本号错误"})
                else:
                    q1.children.append(Q(**{"version_id":list(release_query)[0]['id']}))
        except Exception as e:
            return JsonResponse({"status":40004,"msg":"产品名称或版本号错误"})

    if "status" in req:
        if req["status"] == "all":
            del req["status"]
        elif req["status"] == "notClosed":
            q1.children.append(~Q(**{"status":"Closed"}))
        else:
            status = req["status"]
            q1.children.append(Q(**{"status":status}))

    if "m1_id" in request.GET:
        m1_id = request.GET["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))
        
    if "m2_id" in request.GET:
        m2_id = request.GET["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    if "severity" in req:
        if req["severity"] == "all":
            del req["severity"]

    if "priority" in req:
        if req["priority"] == "all":
            del req["priority"]

    for data in req.items():
        if "product_code" in data or "priority" == data[0] or "severity" in data:
            q1.children.append(Q(**{data[0]: data[1]}))

    if "operate" in req:
        operate = req["operate"]
        if operate == "AssignedByMe":
            conditions.children.append(Q(**{"assignedTo_id":get_uid(request)}))
        if operate == "ResolvedByMe":
            conditions.children.append(Q(**{"fixed_id":get_uid(request)}))
        if operate == "ClosedByMe":
            conditions.children.append(Q(**{"closed_id":get_uid(request)}))
        if operate == "CreatedByMe":
            conditions.children.append(Q(**{"creator_id":get_uid(request)}))
        if operate == "notClosed":
            q1.children.append(~Q(**{"status":"Closed"}))
        if operate == "WaitPending":
            my_group = get_user_group(request)
            if my_group == 'test':
                q2 = Q()
                q2.connector = "AND"
                q2.children.append(Q(**{"assignedTo_id":get_uid(request)}))
                q2.children.append(~Q(**{"status":"closed"}))
                conditions.add(q2, "AND")
            else:
                q2 = Q()
                q2.connector = "AND"
                q2.children.append(Q(**{"assignedTo_id":get_uid(request)}))
                temp_q2_1 = Q()
                temp_q2_1.connector = "OR"
                temp_q2_1.children.append(Q(**{"status":"Open"}))
                temp_q2_1.children.append(Q(**{"status":"Reopen"}))
                temp_q2_1.children.append(Q(**{"status":"Hang-up"}))
                q2.add(temp_q2_1, "AND")
                conditions.add(q2, "AND")
        if operate == "NotResolved":
            q2 = Q()
            q2.connector = "OR"
            q2.children.append(Q(**{"status":"New"}))
            q2.children.append(Q(**{"status":"Open"}))
            q2.children.append(Q(**{"status":"Reopen"}))
            q2.children.append(Q(**{"status":"Hang-up"}))
            conditions.add(q2, "AND")

    if "order" in req:
        order = req["order"]
    else:
        order = "-create_time"
            
    conditions.add(q1, "AND")

    try:
        data = Bug.objects.filter(conditions).\
            annotate(
                creator_user=F("creator_id__realname"),
                assignedTo_user=F("assignedTo_id__realname"),
                fixed_user=F("fixed_id__realname"),
                severity_name=F("severity__name"),
                priority_name=F("priority__name"),
                status_name = F("status__name"),
                solution_name=F("solution__name")
            ).\
            order_by(order).\
            values("id","product_code","bug_id","title","status","status_name","solution_name",\
            "priority","priority_name","severity","severity_name","solution",\
            "creator_id","creator_user","create_time",\
            "assignedTo_user","assignedTo_time",
            "fixed_id","fixed_time","fixed_user",
            "closed_id","closed_time","last_time")
    except Exception as e:
        print(e)
        return JsonResponse({"status":40004,"msg":"异常错误，请联系管理员"})
    else:
        return HttpResponse(get_listing(request.GET, data))

"""
 bug details
"""
@require_http_methods(["GET"])
def details(request):
    try:
        bug_id = request.GET["bug_id"]
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"请求参数错误."})
    
    data = Bug.objects.filter(bug_id=bug_id).\
        annotate(
            creator_user=F("creator_id__realname"),
            assignedTo_user=F("assignedTo_id__realname"),
            fixed_user=F("fixed_id__realname"),
            closed_user=F("closed_id__realname"),
            severity_name=F("severity__name"),
            priority_name=F("priority__name"),
            status_name=F("status__name"),
            solution_name=F("solution__name"),
            release=F("version_id__version"),
            bug_type_name=F("bug_type__name"),
            m1_name=F("m1_id__m1"),
            m2_name=F("m2_id__m2")
        ).\
        values("id","product_code","release","bug_id","m1_name","m2_name","m1_id","m2_id",\
            "title","steps","reality_result","expected_result","remark",\
            "priority","priority_name","severity","severity_name","bug_type",\
            "bug_type_name","solution","solution_name","status","status_name",\
            "creator_id","creator_user","create_time","assignedTo_id","assignedTo_user","assignedTo_time",\
            "fixed_user","fixed_id","fixed_time","closed_user","closed_id","closed_time","case_id","last_time")

    annex = BugAnnex.objects.filter(Q(bug_id=bug_id) & Q(isDelete=0)).values("url")

    annex_tmp = []
    for ax in annex:
        try:
            ax["suffix"] = str(ax["url"]).split('.')[-1]
        except Exception as e:
            ax["suffix"] = "unknow"
        annex_tmp.append(ax)
    
    if len(data) == 0:
        return JsonResponse({"status":20004,"msg":"没找到数据"})
    else:
        return JsonResponse({"status":20000,"data":list(data)[0],"annex":list(annex_tmp)})

"""
 bug delete
"""
@csrf_exempt
@require_http_methods(["GET"])
def delete(request):
    try:
        bug_id = request.GET["bug_id"]
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"请求参数错误."})
    
    try:
        data = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"bug_id不存在"})

    try:
        data.isDelete = 1
        data.status = BugStatus.objects.get(key="Closed")
        data.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"删除失败"})
    else:
        msg = "{0} 删除了缺陷".format(get_user_name(request))
        log = BugHistory(
            bug_id = data,
            desc = msg
            )
        log.save()
        return JsonResponse({"status":20000,"msg":"删除成功"})


"""
  bug create
"""
@csrf_exempt
@require_http_methods(["POST"])
def create(request):

    try:
        req = json.loads(request.body)
        product_code = req["product_code"]
        release = req["release"]
        title = req["title"]
        steps = req["steps"]
        reality_result = req["reality_result"]
        expected_result = req["expected_result"]
        priority = req["priority"]
        severity = req["severity"]
        assignedTo = req["assignedTo_id"]
        annex = req["annex"]
        bug_type = req["bug_type"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的参数"})

    m1_id,m2_id = None,None
    if "module_id" in req and req["module_id"]:
        try:
            m1_id = ModuleA.objects.get(id=req["module_id"][0])
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})

        if len(req["module_id"]) == 2:
            try:
                m2_id = req["module_id"][1]
                m2_id = ModuleB.objects.get(id=m2_id)
            except Exception as e:
                return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
        
    try:
        if "case_id" in req and req["case_id"]:
            case_id = req["case_id"]
            case_obj = TestCase.objects.get(case_id=case_id)
        else:
            case_obj = None
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"case_id无效"})
        
    try:
        if "cell_id" in req and req["cell_id"]:
            cell_id = req["cell_id"]
            cell_obj = TestSuiteCell.objects.get(cell_id=cell_id)
        else:
            cell_obj = None
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"cell_id无效"})

    if assignedTo:
        assignedTo = req["assignedTo_id"]
        try:
            assignedTo_object = User.objects.get(user_id=assignedTo)
        except Exception as e:
            return JsonResponse({"status":40004,"msg":"指派人不存在"})
        assignedToDate = curremt_time
        status = BugStatus.objects.get(key="Open")
    else:
        assignedTo_object = None
        assignedToDate = None
        status = BugStatus.objects.get(key="New")
    
    # product_code
    try:
        product_object = Product.objects.get(product_code=product_code)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"产品名称无效"})

    # version_object
    try:
        version_object = Release.objects.get(Q(product_code=product_code) & Q(version=release))
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"版本号无效"})

    # priority
    try:
        priority_object = BugPriority.objects.get(key=priority)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"优先级值无效"})

    # severity
    try:
        severity_object = BugSeverity.objects.get(key=severity)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"严重程度值无效"})

    # BugType
    try:
        bug_type_object = BugType.objects.get(key=bug_type)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"缺陷类型无效"})

    # remark
    if "remark" in req:
        remark = req["remark"]
    else:
        remark = ""

    try:
        bug = Bug(
            product_code = product_object,
            version_id = version_object,
            priority = priority_object,
            severity = severity_object,
            bug_type = bug_type_object,
            creator_id = get_user_object(request),
            title = title,
            steps = steps,
            reality_result = reality_result,
            expected_result = expected_result,
            assignedTo_id = assignedTo_object,
            assignedTo_time = assignedToDate,
            remark = remark,
            status = status,
            case_id = case_obj,
            cell_id = cell_obj,
            m1_id = m1_id,
            m2_id = m2_id
        )
        bug.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"提交bug失败"})
    else:
        bug_id = Bug.objects.get(bug_id=bug.bug_id)
        # 记录日志
        try:
            bug_log_record(request,get_user_object(request),bug_id,"create")
        except Exception as e:
            pass

        # 保存附件
        try:
            if annex:
                for f in annex:
                    aex = BugAnnex(
                        bug_id = bug_id,
                        url = f
                        )
                    aex.save()
        except Exception as e:
            Bug.objects.get(bug_id=bug_id).delete()
            return JsonResponse({"status":20004,"msg":"bug附件错误"})
        else:
            return JsonResponse({"status":20000,"msg":"缺陷保存成功"})

"""
  bug edit
"""
@csrf_exempt
@require_http_methods(["POST"])
def edit(request):
    try:
        req = json.loads(request.body)
        bug_id = req["bug_id"]
        bug_obj = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少bug_id或bug_id无效"})

    if "assignedTo_id" in req:
        try:
            bug_obj.assignedTo_id = User.objects.get(user_id=req["assignedTo_id"])
            bug_obj.assignedTo_time = curremt_time
        except Exception as e:
            print(e)
            return JsonResponse({"status":40001,"msg":"指派人不存在"})
        else:
            status = Bug.objects.filter(bug_id=bug_id).values_list("status")[0]
            if status == 'New':
                bug_obj.status = BugStatus.objects.get(key="Open")

    # check product_code
    if "product_code" in req:
        try:
            bug_obj.product_code = Product.objects.get(product_code=req["product_code"])
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":"产品名称无效"})

    if "module_id" in req and req["module_id"]:
        try:
            m1_id = ModuleA.objects.get(id=req["module_id"][0])
            bug_obj.m1_id = m1_id
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
            
        if len(req["module_id"]) == 2:
            try:
                m2_id = req["module_id"][1]
                bug_obj.m2_id = ModuleB.objects.get(id=m2_id)
            except Exception as e:
                return JsonResponse({"status": 40004, "msg": u"产品模块无效."})

    # check version_object
    if "release" in req:
        if "product_code" not in req:
            return JsonResponse({"status":40001,"msg":"当您修改版本信息时，必须提交产品选项"})
        try:
            bug_obj.version_id = Release.objects.get(Q(product_code=req["product_code"]) & Q(version=req["release"]))
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":"版本号无效"})

    # check priority
    if "priority" in req:
        try:
            bug_obj.priority = BugPriority.objects.get(key=req["priority"])
        except Exception as e:
            return JsonResponse({"status":40004,"msg":"优先级值无效"})

    # check severity
    if "severity" in req:
        try:
            bug_obj.severity = BugSeverity.objects.get(key=req["severity"])
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":"严重程度值无效"})

    # check BugType
    if "bug_type" in req:
        try:
            bug_obj.bug_type = BugType.objects.get(key=req["bug_type"])
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":"缺陷类型无效"})

    if "title" in req:
        bug_obj.title = req["title"]
    if "steps" in req:
        bug_obj.steps = req["steps"]
    if "reality_result" in req:
        bug_obj.reality_result = req["reality_result"]
    if "expected_result" in req:
        bug_obj.expected_result = req["expected_result"]
    if "remark" in req:
        bug_obj.remark = req["remark"]

    try:
        bug_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"缺陷修改失败"})
    else:
        # 记录日志
        try:
            bug_log_record(request,get_user_object(request),bug_obj,"edit")
        except Exception as e:
            print(e)
            pass
        # 保存附件
        try:
            if "annex" in req:
                annex = req["annex"]
                for f in annex:
                    aex = BugAnnex(
                        bug_id = bug_obj,
                        url = f
                        )
                    aex.save()
        except Exception as e:
            print(e)
            return JsonResponse({"status":20004,"msg":"bug附件错误"})
        else:
            return JsonResponse({"status":20000,"msg":"修改成功"})

"""
  bug: 附件删除
"""
@csrf_exempt
@require_http_methods(["POST"])
def annex_delete(request):
    try:
        req = json.loads(request.body)
        url = req["url"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"附件url不能为空哦"})
    
    try:
        ba_obj = BugAnnex.objects.get(url=url)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"没找到数据"})
    try:
        ba_obj.isDelete = 1
        ba_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"附件删除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"附件删除成功"})

"""
  修复bug,解决方案
"""
@csrf_exempt
@require_http_methods(["POST"])
def resolve(request):
    try:
        req = json.loads(request.body)
        bug_id = req["bug_id"]
        solution = req["solution"]
        assignedTo = req["assignedTo"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的参数"})

    try:
        assignedTo_obj = User.objects.get(user_id=assignedTo)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"指派人不存在"})

    if "remark" in req:
        remark = req["remark"]
        if len(remark) > 1000:
            return JsonResponse({"status":40004,"msg":"备注的有效长度为1000"})
    else:
        remark = ""

    try:
        bug_object = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"bug_id无效"})

    try:
        is_solution = BugSolution.objects.get(key=solution)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"solution无效"})

    try:
        user_obj = get_user_object(request)
        bug_object.solution = is_solution
        bug_object.assignedTo_id = assignedTo_obj
        bug_object.fixed_id = user_obj
        bug_object.fixed_time = curremt_time
        bug_object.status = BugStatus.objects.get(key="Fixed")
        bug_object.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"提交失败"})
    else:
        Solution_content = BugSolution.objects.filter(key=solution).values_list("name",flat=True)[0]
        msg = "解决了缺陷。解决方案为：{0}".format(Solution_content)
        log = BugHistory(
            user_id = user_obj,
            bug_id = bug_object,
            desc = msg,
            remark = remark
            )
        log.save()
        return JsonResponse({"status":20000,"msg":"提交成功"})


"""
  bug 分配
"""
@csrf_exempt
@require_http_methods(["POST"])
def assign(request):
    try:
        req = json.loads(request.body)
        bug_id = req["bug_id"]
        assignedTo = req["assignedTo"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的参数"})

    try:
        assignedTo_obj = User.objects.get(user_id=assignedTo)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"分配的用户不存在"})

    try:
        bug_obj = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"bug_id无效"})

    if "remark" in req:
        remark = req["remark"]
        if len(remark) > 1000:
            return JsonResponse({"status":40004,"msg":"备注的有效长度为1000"})
    else:
        remark = ""

    try:
        bug_obj.assignedTo_id = assignedTo_obj
        bug_obj.assignedTo_time = curremt_time
        bug_obj.status = BugStatus.objects.get(key="Open")
        bug_obj.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"分配失败"})
    else:
        assignedTo_user = User.objects.filter(user_id=assignedTo).values_list("realname",flat=True)
        msg = "指派给：{0}".format(assignedTo_user[0])
        log = BugHistory(
            user_id = get_user_object(request),
            bug_id = bug_obj,
            desc = msg,
            remark = remark
            )
        log.save()
        return JsonResponse({"status":20000,"msg":"分配成功"})

"""
  bug history
"""
def history(request):
    try:
        bug_id = request.GET["bug_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的请求参数"})

    data = BugHistory.objects.filter(bug_id=bug_id).\
        annotate(
            username = F("user_id__realname")
            ).\
        order_by("create_time").\
        values("create_time","desc","username","remark")

    return JsonResponse({"status":20000,"data":list(data)})



"""
  bug close
"""
@csrf_exempt
@require_http_methods(["POST"])
def close(request):
    try:
        req = json.loads(request.body)
        bug_id = req["bug_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的请求参数"})

    try:
        bug_object = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"bug_id无效"})

    try:
        bug_object.status = BugStatus.objects.get(key="Closed")
        bug_object.closed_id = get_user_object(request)
        bug_object.closed_time = curremt_time
        bug_object.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"缺陷关闭失败"})
    else:
        bug_log_record(request,get_user_object(request),bug_object,"close")
        return JsonResponse({"status":20000,"msg":"缺陷关闭成功"})


"""
 bug reopen
"""
@csrf_exempt
@require_http_methods(["POST"])
def reopen(request):
    try:
        req = json.loads(request.body)
        bug_id = req["bug_id"]
        assignedTo = req["assignedTo"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的请求参数"})

    remark = ""
    if "remark" in req:
        remark = req["remark"]
        if len(remark) > 1000:
            return JsonResponse({"status":40004,"msg":"备注的有效长度为1000"})

    try:
        bug_object = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"bug_id无效"})

    try:
        assignedTo_obj = User.objects.get(user_id=assignedTo)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"分配的用户不存在"})

    try:
        bug_object.status = BugStatus.objects.get(key="Reopen")
        bug_object.assignedTo_id = assignedTo_obj
        bug_object.assignedTo_time = curremt_time
        bug_object.solution = None
        bug_object.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"重新打开失败"})
    else:
        assignedTo_user = User.objects.filter(user_id=assignedTo).values_list("realname",flat=True)[0]
        msg = "重新打开缺陷。并分配给：{0}".format(assignedTo_user)
        log = BugHistory(
            user_id = get_user_object(request),
            bug_id = bug_object,
            desc = msg,
            remark = remark
            )
        log.save()
        return JsonResponse({"status":20000,"msg":"缺陷重新打开成功"})


"""
  挂起
"""
@csrf_exempt
@require_http_methods(["POST"])
def hangup(request):
    try:
        req = json.loads(request.body)
        bug_id = req["bug_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺陷ID不能为空"})

    try:
        bug_object = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"bug_id无效"})

    try:
        bug_object.status = BugStatus.objects.get(key="Hang-up")
        bug_object.hangUp_id = get_user_object(request)
        bug_object.hangUp_time = curremt_time
        bug_object.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"延期操作失败"})
    else:
        bug_log_record(request,get_user_object(request),bug_object,"Hang-up")
        return JsonResponse({"status":20000,"msg":"延期操作成功"})

"""
  bug remark
"""
@csrf_exempt
@require_http_methods(["POST"])
def add_notes(request):
    try:
        req = json.loads(request.body)
        bug_id = req["bug_id"]
        remark = req["remark"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺陷ID和备注不能为空"})
    else:
        if len(remark) == 0 or len(remark) > 2000:
            return JsonResponse({"status":40001,"msg":"备注的有效长度为1-2000"})

    try:
        bug_object = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"bug_id无效"})

    try:
        msg = "添加了备注。"
        notes = BugHistory(
            bug_id = bug_object,
            remark = remark,
            desc = msg,
            user_id = get_user_object(request)
            )
        notes.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"提交失败"})
    else:
        return JsonResponse({"status":20000,"msg":"提交成功"})

"""
  bug: report
"""
@require_http_methods(["GET"])
def bug_report(request):

    today = time.strftime("%Y-%m-%d", time.localtime())
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        req = request.GET
        product_code = req["product_code"]
        t = req["type"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要请求参数"})
    
    # today bug data
    status_data = []
    create = Bug.objects.filter(Q(create_time__gte=today) & Q(product_code=product_code)).\
        aggregate(create=Count("create_time"))
    status_data.append(create)

    closed = Bug.objects.\
        filter(Q(closed_time__gte=today) & Q(status="Closed") & Q(product_code=product_code)).\
        aggregate(closed=Count("closed_time"))
    status_data.append(closed)
    
    fixed = Bug.objects.\
        filter(Q(fixed_time__gte=today) & Q(status="Fixed") & Q(product_code=product_code)).\
        aggregate(hangUp=Count("fixed_time"))
    status_data.append(fixed)

    hangUp = Bug.objects.\
        filter(Q(hangUp_time__gte=today) & Q(status="HangUp") & Q(product_code=product_code)).\
        aggregate(hangUp=Count("hangUp_time"))
    status_data.append(hangUp)

    # surplus no fixed bug
    surplus_bug = Bug.objects.\
        filter(Q(product_code=product_code) & ~Q(status="Closed") & ~Q(status="Fixed")).\
        annotate(name = F("severity__name")).\
        values("name").annotate(value=Count("id")).order_by("-value")

    # 致命一级bug
    fatal_bug = Bug.objects.filter(Q(product_code=product_code) & Q(severity="Fatal")).order_by("id").\
        values("id","title")

    today_data = {
        "datetime": get_time,
        "product_code":product_code,
        "status_data":status_data,
        "surplus_bug":list(surplus_bug),
        "fatal_bug":list(fatal_bug)
    }
    try:
        report = BugReport(
            content = json.dumps(today_data)
        )
        report.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"出现错误了，请联系管理员"})
    else:
        return JsonResponse({"status":20000,"report_id":report.report_id,"msg":"已成功生成今天的缺陷日报"})

"""
  bug: report details
"""
@require_http_methods(["GET"])
def report_details(request):
    try:
        req = request.GET
        report_id = req["report_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"report_id不能为空"})

    try:
        data = BugReport.objects.filter(report_id=report_id).values("content")
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"报告获取失败"})
    else:
        t = list(data)[0]["content"]
        return JsonResponse({"status":20000,"data":t})


"""
  bug export
"""
@require_http_methods(["GET"])
def export(request):

    q1 = Q()
    q1.connector = "AND"

    try:
        req = request.GET.dict()
        product_code = req["product_code"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"产品名称不能为空"})
    else:
        q1.children.append(Q(**{"product_code":product_code}))
    print(req)
    if "release" in req:
        try:
            release = req["release"]
            if release == "all":
                del req["release"]
            else:
                release_query = Release.objects.filter(Q(product_code=product_code) & Q(version=release)).values('id')
                if len(release_query) == 0:
                    return JsonResponse({"status":40004,"msg":"版本号错误"})
                else:
                    q1.children.append(Q(**{"version_id":list(release_query)[0]['id']}))
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":"产品名称或版本号错误"})

    if "status" in req:
        if req["status"] == "all":
            del req["status"]
        elif req["status"] == "notClosed":
            q1.children.append(~Q(**{"status":"Closed"}))
        else:
            status = req["status"]
            q1.children.append(Q(**{"status":status}))

    bug_data = Bug.objects.filter(q1).\
        annotate(
                creator_user=F("creator_id__realname"),
                assignedTo_user=F("assignedTo_id__realname"),
                fixed_user=F("fixed_id__realname"),
                closed_user=F("closed_id__realname"),
                severity_name=F("severity__name"),
                status_name = F("status__name"),
                solution_name=F("solution__name"),
                release=F("version_id__version"),
                bug_type_name=F("bug_type__name"),
                m1_name=F("m1_id__m1"),
                m2_name=F("m2_id__m2")
            ).\
        order_by("-id").\
        values_list("id","product_code","release","m1_name","title","status_name",
            "priority","severity_name","solution_name",\
            "creator_user","create_time","assignedTo_user","assignedTo_time",\
            "fixed_user","fixed_time","closed_user","closed_time","bug_type_name")[:]

    if len(bug_data) == 0:
        return JsonResponse({"status":20004,"msg":"没有查到相关数据,请修改查询条件"})

    # 准备行数据
    # table_data = bug_data
    # field_length = len(bug_data[0])

    # 整理列数据
    table_data = []
    field_length = len(bug_data[0])
    for n in range(0,field_length):
        temp = []
        for item in bug_data:
            temp.append(item[n])
        table_data.append(temp)
    
    try:
        filename = 'Bug_{0}_{1}.xlsx'.format(product_code,visualtime)
        filepath = 'media/export/' + filename
        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet('Bug')

        # 工作表头部
        header_name = ['id','产品','版本','模块','标题','状态','优先级','严重程度',
            '解决方案','创建人','创建时间','指派给谁','指派时间','解决者','修复时间','关闭者','关闭时间','缺陷类型']
        cell_head = 'A1:{0}1'.format(string.ascii_uppercase[field_length])

        cell_head_format = workbook.add_format({
            "bold": True,
            "font_size": 13,
            "fg_color": "#EEEEEE",
            "locked":"True",
            'align':'vcenter'
            })
        worksheet.write_row(cell_head,header_name,cell_head_format)

        # 单元格高度
        cell_format = workbook.add_format({
            'align':'vcenter'
        })
        for row in range(0,len(bug_data)+1):
            worksheet.set_row(row, 28)

        # 单元格宽度
        worksheet.set_column('E:E',80)
        worksheet.set_column('K:K',15)
        worksheet.set_column('M:M',15)
        worksheet.set_column('O:O',15)
        worksheet.set_column('Q:Q',15)

        # 缺陷状态栏，按条件筛选
        caption = ('Cells with values == 1 are in light red. '
           'Values > 100 are in light green.')
        for n in range(2,len(bug_data)):
            print('A'+ str(n))
            worksheet.write('A'+ str(n), caption)

        # 按行写入
        # rows_num = len(table_data) + 1
        # rows = [ 'A' + str(i) for i in range(2,rows_num)]
        # for i,element in enumerate(rows):
        #     worksheet.write_row(element,table_data[i],cell_format)

        # 按列写入
        columns = [ chr(i) + '2' for i in range(65,65 + int(field_length))]

        for i,element in enumerate(columns):
            # 日期时间单元格格式
            if element in ['K2','M2','O2','Q2']:
                cell_date_format = workbook.add_format({
                    'num_format':'yyyy/mm/dd hh:mm',
                    'align':'vcenter'
                })
                worksheet.write_column(element,table_data[i],cell_date_format)
            else:
                worksheet.write_column(element,table_data[i],cell_format)
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"导出Excel时，写入文件失败"})
    else:
        workbook.close()
        return JsonResponse({"status":20000,"filename":filename,"url":"/"+filepath})