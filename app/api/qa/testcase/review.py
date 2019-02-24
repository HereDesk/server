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
from app.models import TestCaseReview

from app.api.auth import get_user_object

visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())

"""
  评审
"""
@csrf_exempt
@require_http_methods(["POST"])
def review(request):

    try:
        req = json.loads(request.body)
        case_id = req["case_id"]
        result = req["result"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"Result和case_id不能为空"})

    if result in [1,2]:
        pass
    else:
        return JsonResponse({"status":40001,"msg":"Result无效"})

    if "remark" in req:
        remark = req["remark"]
    else:
        remark = ""

    try:
        case_obj = TestCase.objects.get(case_id=case_id)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"case_id无效"})

    try:
        case_obj.isReview = result
        case_obj.save()

        review_result = TestCaseReview(
            user_id = get_user_object(request),
            case_id = case_obj,
            result = result,
            remark = remark
            )
        review_result.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"操作失败"})
    else:
        return JsonResponse({"status":20000,"msg":"操作成功"})