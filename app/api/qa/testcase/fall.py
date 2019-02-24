#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import TestCase
from app.models import TestCaseFiles

from app.api.utils import get_listing
from app.api.auth import get_user_object

visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())


"""
  测试用例：失效操作
"""
@csrf_exempt
@require_http_methods(["GET"])
def fall(request):
    try:
        case_id = request.GET["case_id"]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"case_id不能为空"})

    try:
        case_id = TestCase.objects.get(case_id=case_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"case_id无效"})

    try:
        case_id.status = 1
        case_id.faller_id = get_user_object(request)
        case_id.fall_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        case_id.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"操作失败"})
    else:
        return JsonResponse({"status":20000,"msg":"操作成功"})