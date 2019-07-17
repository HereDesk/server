#!/usr/bin/env python
# -*- coding:utf8 -*-
import json

from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Bug
from app.models import BugHistory

from app.api.auth import get_user_name


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
        data.is_delete = 1
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