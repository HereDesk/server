#!/usr/bin/env python
# -*- coding:utf8 -*-

import json

from django.http import JsonResponse
from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import User

from app.models import Bug
from app.models import BugAnnex
from app.models import BugHistory


"""
  bug: 附件删除
"""
@csrf_exempt
@require_http_methods(["POST"])
def delete(request):
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
        ba_obj.is_delete = 1
        ba_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"附件删除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"附件删除成功"})