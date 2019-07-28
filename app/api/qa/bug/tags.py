#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from datetime import datetime

from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Bug

"""
  bug create
"""
@csrf_exempt
@require_http_methods(["POST"])
def add(request):
    try:
        req = json.loads(request.body)
        bug_id = req["bug_id"]
        tag_name = req["tag_name"]
        bug_obj = Bug.objects.get(bug_id=bug_id)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"缺少bug_id或bug_id无效"})

    if len(tag_name) > 6:
        return JsonResponse({"status":20004,"msg":"标签长度不要超过6"})

    try:
        bug_obj.bug_label=tag_name
        bug_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"服务端异常，保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"缺陷标签创建成功"})

