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

from app.api.utils import get_listing
from app.api.auth import get_user_object

visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())

"""
  搜索结果
"""
@csrf_exempt
@require_http_methods(["GET"])
def search(request):

    try:
        wd = request.GET["wd"]
        product_id = request.GET["product_id"]
    except Exception as e:
         return JsonResponse({"status": 40004, "msg": u"请求参数错误."})

    if "status" in request.GET:
        status = request.GET["status"]
    else:
        status = 0

    try:
        data = TestCase.objects.\
            filter(Q(product_id=product_id) &
                Q(status=status) &
                Q(is_delete=0) & (
                Q(title__icontains=wd) | 
                Q(id__icontains=wd))
                ).\
            annotate(
                creator=F("creator_id__realname")
                ).\
            values("id","case_id","product_id","status","title","priority",
                "is_change","is_review","creator","creator_id","create_time","last_time")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        if len(data) == 0:
            return JsonResponse({"status": 20001, "msg": "根据搜索条件，没有查到数据"})
        else:
            return HttpResponse(get_listing(request.GET,data))
