#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from datetime import datetime

from django.http import JsonResponse
from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import BugType
from app.models import BugStatus
from app.models import BugPriority
from app.models import BugSeverity
from app.models import BugSource
from app.models import BugSolution

from app.models import BugHistory

# 日志记录
def bug_log_record(request,userId,bug_id,status):

    req = json.loads(request.body)
    
    if "remark" in req:
        remark = req["remark"]
    else:
        remark = ""

    if len(remark) > 2000:
        return JsonResponse({"status":40004,"msg":"长度超出。"})
        
    msg = ""
    if status == "create":
        msg = "创建了缺陷。"
        remark = ""

    if status == "close":
        msg = "关闭了缺陷。"

    if status == "Hang-up":
        msg = "将缺陷挂起。"
    
    if status == "edit":
        del req["bug_id"]
        if len(req) == 1 and "priority" in req:
            msg = "修改缺陷优先级为：{0}。".format(req["priority"])
        elif len(req) == 1 and "severity" in req:
            msg = "修改了严重程度。"
        else:
            msg = "修改了缺陷。"
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
 缺陷: 类型、优先级、严重程度、来源、解决方案
"""
@require_http_methods(["GET"])
def property(request):

    try:
        # bug type
        bug_type = BugType.objects.all().values("key","name")

        # bug priority
        bug_priority = BugPriority.objects.all().values("key","name")

        # bug severity
        bug_severity = BugSeverity.objects.all().values("key","name")

        # bug source
        bug_source = BugSource.objects.all().values("key","name")

        # bug solution
        bug_solution = BugSolution.objects.all().values("key","name") 
        
    except Exception as e:
        return JsonResponse({
            "status":40004,
            "msg":"系统出错了"
            })
    else:
        return JsonResponse({
            "status":20000,
            "bug_type":list(bug_type),
            "bug_priority":list(bug_priority),
            "bug_severity":list(bug_severity),
            "bug_source":list(bug_source),
            "bug_solution": list(bug_solution)
            })

