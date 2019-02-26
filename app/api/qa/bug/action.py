#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time

from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F

from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import User

from app.models import BugType
from app.models import BugStatus
from app.models import BugPriority
from app.models import BugSeverity
from app.models import BugSolution
from app.models import BugSource

from app.models import Bug
from app.models import BugAnnex
from app.models import BugHistory
from app.models import BugReport

from app.api.auth import get_user_object
from app.api.qa.bug.support import bug_log_record

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
        bug_object.last_operation = get_user_object(request)
        bug_object.solution = is_solution
        bug_object.assignedTo_id = assignedTo_obj
        bug_object.fixed_id = get_user_object(request)
        bug_object.fixed_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        bug_object.status = BugStatus.objects.get(key="Fixed")
        bug_object.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"提交失败"})
    else:
        Solution_content = BugSolution.objects.filter(key=solution).values_list("name",flat=True)[0]
        msg = "解决了缺陷。解决方案为：{0}".format(Solution_content)
        log = BugHistory(
            user_id = get_user_object(request),
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
        bug_obj.last_operation = get_user_object(request)
        bug_obj.assignedTo_id = assignedTo_obj
        bug_obj.assignedTo_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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
        bug_object.last_operation = get_user_object(request)
        bug_object.status = BugStatus.objects.get(key="Closed")
        bug_object.closed_id = get_user_object(request)
        bug_object.closed_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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
        bug_object.last_operation = get_user_object(request)
        bug_object.status = BugStatus.objects.get(key="Reopen")
        bug_object.assignedTo_id = assignedTo_obj
        bug_object.assignedTo_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        bug_object.solution = None
        bug_object.closed_id = None
        bug_object.closed_time = None
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
        bug_object.last_operation = get_user_object(request)
        bug_object.status = BugStatus.objects.get(key="Hang-up")
        bug_object.hangUp_id = get_user_object(request)
        bug_object.hangUp_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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
def remarks(request):
    req = json.loads(request.body)

    if "record_id" not in req:
        try:
            
            bug_id = req["bug_id"]
            remark = req["remark"]
        except Exception as e:
            return JsonResponse({"status":40001,"msg":"缺陷ID和备注不能为空"})
        else:
            if len(remark) == 0 or len(remark) > 2000:
                return JsonResponse({"status":40001,"msg":"备注的有效长度为1-2000"})

        try:
            bug_object = Bug.objects.get(bug_id=bug_id)
            bug_object.last_operation = get_user_object(request)
            bug_object.save()
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
    else:
        try:
            bug_id = req["bug_id"]
            record_id = req["record_id"]
            remark = req["remark"]
        except Exception as e:
            return JsonResponse({"status":40001,"msg":"ID和备注不能为空"})

        try:
            record_object = BugHistory.objects.get(record_id=record_id)
        except Exception as e:
            return JsonResponse({"status":40004,"msg":"ID无效"})

        try:
            bug_object = Bug.objects.get(bug_id=bug_id)
            bug_object.last_operation = get_user_object(request)
            bug_object.save()
        except Exception as e:
            return JsonResponse({"status":40004,"msg":"bug_id无效"})

        try:
            if len(remark) == 0:
                record_object.remark_status = 0
            else:
                record_object.remark_status = 2
                record_object.remark = remark
            record_object.save()
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"修改失败"})
        else:
            return JsonResponse({"status":20000,"msg":"修改成功"})

