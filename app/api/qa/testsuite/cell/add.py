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
  test suite cell add 
"""
@csrf_exempt
@require_http_methods(["POST"])
def add(request):
    try:
        req = json.loads(request.body)
        suite_id = req["suite_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"suite_id不能为空"})
    
    if "case_data" in req and "m1" not in req:
        case_data = req["case_data"]
    if "case_data" in req and "m1" in req:
        return JsonResponse({"status":40001,"msg":"请检查请求数据"})

    if "m1" in req:
        m1 = req["m1"]
        if "m2" in req:
            m2 = req["m2"]
            case_data = TestCase.objects.filter(Q(m2_id=m2)).values_list("case_id")[:]
        else:
            case_data = TestCase.objects.filter(Q(m1_id=m1)).values_list("case_id")[:]
        if len(case_data) == 0:
            return JsonResponse({"status":20004,"msg":"该模块下没有测试用例数据"})
        case_data = [ str(i[0]) for i in case_data]

    if len(case_data) == 0:
        return JsonResponse({"status":20004,"msg":"没有选中用例哦"})

    get_exist_data = TestSuiteCell.objects.filter(Q(suite_id=suite_id)).values_list("case_id")

    if get_exist_data:
        get_exist_data = [ str(i[0]) for i in get_exist_data ]

    after_case_data = [case for case in case_data if case not in get_exist_data]

    if len(after_case_data) == 0:
        return JsonResponse({"status":20004,"msg":"已存在，请选择其它用例"})
        
    try:
        creator_obj = get_user_object(request)
        suite_obj = TestSuite.objects.get(suite_id=suite_id)
        try:
            data = [ TestSuiteCell(
                case_id = TestCase.objects.get(case_id=i),
                suite_id = suite_obj,
                creator_id = creator_obj)
                for i in after_case_data ]
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"用例ID无效"})
        else:
            TestSuiteCell.objects.bulk_create(data)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"保存失败，请联系管理员"})
    else:
        return JsonResponse({"status":20000,"msg":"保存成功"})