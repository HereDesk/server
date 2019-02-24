#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
import uuid
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count
from django.db.models import Sum
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import ProductMembers

from app.models import Authentication

from app.models import Bug
from app.models import TestCase
from app.models import TestSuite
from app.models import TestSuiteCell

from app.api.utils import get_listing
from app.api.auth import get_uid
from app.api.auth import get_user_object

# get cureent time
curremt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


"""
  test suite cell run
"""
@csrf_exempt
@require_http_methods(["POST"])
def run(request):
    try:
        req = json.loads(request.body)
        cell_id = req["cell_id"]
        result = req["result"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"cell_id和result不能为空"})
    
    if result == 1 or result == -1:
        pass
    else:
        JsonResponse({"status":40001,"msg":"result无效"})

    try:
        cell_obj = TestSuiteCell.objects.get(cell_id=cell_id)
        cell_obj.result = result
        cell_obj.runner_id = get_user_object(request)
        cell_obj.run_time = curremt_time
        cell_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"服务器开小差了"})
    else:
        return JsonResponse({"status":20000,"msg":"用例运行结果保存成功"})