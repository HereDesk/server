#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from datetime import datetime

from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count
from django.db.models import Max

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release

from app.models import ModuleA
from app.models import ModuleB

from app.models import User

from app.models import BugType
from app.models import BugStatus
from app.models import BugPriority
from app.models import BugSeverity
from app.models import BugSolution
from app.models import BugSource

from app.models import Bug
from app.models import BugAnnex

from app.api.auth import get_user_object
from app.api.qa.bug.support import bug_log_record

"""
  bug create
"""
@csrf_exempt
@require_http_methods(["POST"])
def create(request):

    try:
        req = json.loads(request.body)
        product_id = req["product_id"]
        release = req["release"]
        title = req["title"]
        steps = req["steps"]
        reality_result = req["reality_result"]
        expected_result = req["expected_result"]
        assignedTo = req["assignedTo_id"]
        annex = req["annex"]
        priority = req["priority"]
        severity = req["severity"]
        bug_type = req["bug_type"]
        bug_source = req["bug_source"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的参数"})

    m1_obj,m2_obj = None,None
    if "module_id" in req and req["module_id"]:
        try:
            m1_obj = ModuleA.objects.get(m1_id=req["module_id"][0])
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
        try:
            if len(req["module_id"]) == 2:
                m2_id = req["module_id"][1]
                m2_obj = ModuleB.objects.get(m2_id=m2_id)
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
        assignedToDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        status = BugStatus.objects.get(key="Open")
    else:
        assignedTo_object = None
        assignedToDate = None
        status = BugStatus.objects.get(key="New")

    # product_code
    try:
        product_object = Product.objects.get(product_id=product_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"产品名称无效"})

    # version_object
    try:
        version_object = Release.objects.get(Q(product_id=product_id) & Q(version=release))
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

    # BugType
    try:
        bug_source_object = BugSource.objects.get(key=bug_source)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"缺陷来源无效"})

    # remark
    if "remark" in req:
        remark = req["remark"]
    else:
        remark = ""

    try:
        # 缺陷辅助ID
        aided_id = Bug.objects.filter(product_id=product_id).aggregate(Max('id'))
        if not aided_id["id__max"]:
            aided_id = 1
        else:
            aided_id = int(aided_id["id__max"]) + 1
        bug = Bug(
            product_id = product_object,
            version_id = version_object,
            priority = priority_object,
            severity = severity_object,
            bug_type = bug_type_object,
            bug_source = bug_source_object,
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
            m1_id = m1_obj,
            m2_id = m2_obj,
            last_operation = get_user_object(request),
            id = aided_id
        )
        bug.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"提交bug失败"})
    else:
        bobj = Bug.objects.get(bug_id=bug.bug_id)


        # 记录日志
        try:
            bug_log_record(request,get_user_object(request),bobj,"create")
        except Exception as e:
            pass

        try:
            if annex:
                for f in annex:
                    aex = BugAnnex(
                        bug_id = bobj,
                        url = f
                        )
                    aex.save()
        except Exception as e:
            Bug.objects.get(bug_id=bobj).delete()
            return JsonResponse({"status":20004,"msg":"bug附件保存错误"})
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
            bug_obj.assignedTo_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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
            bug_obj.product_id = Product.objects.get(product_id=req["product_id"])
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":"产品名称无效"})

    if "module_id" in req and req["module_id"]:
        try:
            m1_obj = ModuleA.objects.get(m1_id=req["module_id"][0])
            bug_obj.m1_id = m1_obj
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})

        if len(req["module_id"]) == 2:
            try:
                m2_obj = ModuleB.objects.get(m2_id=req["module_id"][1])
                bug_obj.m2_id = m2_obj
            except Exception as e:
                return JsonResponse({"status": 40004, "msg": u"产品模块无效."})

    # check version_object
    if "release" in req:
        if "product_id" not in req:
            return JsonResponse({"status":40001,"msg":"当您修改版本信息时，必须提交产品选项"})
        try:
            bug_obj.version_id = Release.objects.get(Q(product_id=req["product_id"]) & Q(version=req["release"]))
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

    # check BugType
    if "bug_source" in req:
        try:
            bug_obj.bug_source = BugSource.objects.get(key=req["bug_source"])
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":"缺陷来源无效"})

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
        bug_obj.last_operation = get_user_object(request)
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
