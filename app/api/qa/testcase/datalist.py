#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import TestCase

from app.api.utils import get_listing

"""
 测试用例LIST
"""
@csrf_exempt
@require_http_methods(["GET"])
def data_list(request):
    q1 = Q()
    q1.connector = "AND"

    try:
        product_id = request.GET["product_id"]
        q1.children.append(Q(**{"product_id":product_id}))
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求值"})

    if "m1_id" in request.GET:
        m1_id = request.GET["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))

    if "m2_id" in request.GET:
        m2_id = request.GET["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    if "status" in request.GET:
        status = request.GET["status"]
        q1.children.append(Q(**{"status":status}))
            
    try:
        data = TestCase.objects.\
            filter(q1).\
            annotate(
                creator=F("creator_id__realname")
                ).\
            values("id","case_id","product_id","status","title","priority",\
                "is_change","is_review",\
                "creator","creator_id","create_time","last_time").\
            order_by("-create_time")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询发生异常错误，请联系管理员."})
    else:
        return HttpResponse(get_listing(request.GET,data))

"""
 测试用例LIST
"""
@csrf_exempt
@require_http_methods(["GET"])
def valid_list(request):
    q1 = Q()
    q1.connector = "AND"

    try:
        product_id = request.GET["product_id"]
        q1.children.append(Q(**{"product_id":product_id}))
    except Exception as e:
        print(e)
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求值"})

    if "m2_id" in request.GET:
        m2_id = request.GET["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    if "m1_id" in request.GET:
        m1_id = request.GET["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))
            
    try:
        q1.children.append(Q(**{"is_delete":0}))
        q1.children.append(Q(**{"status":0}))
        data = TestCase.objects.\
            filter(q1).\
            values("id","case_id","title").order_by("id")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        return HttpResponse(get_listing(request.GET,data))