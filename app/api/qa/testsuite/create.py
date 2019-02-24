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
testcase stuie add
"""
@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    try:
        req = json.loads(request.body)
        product_id = req["product_id"]
        suite_name = req["suite_name"]
        product_obj = Product.objects.get(product_id=product_id)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的请求参数"})

    if len(suite_name) > 30:
        return JsonResponse({"status":20004,"msg":"名称的有效长度需小于30"})
    
    try:
        suite_obj = TestSuite(
            suite_name = suite_name,
            product_id = product_obj,
            creator_id = get_user_object(request)
        )
        suite_obj.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"保存失败，请联系管理员"})
    else:
        return JsonResponse({"status":20000,"msg":"创建成功"})