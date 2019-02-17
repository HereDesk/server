#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from datetime import datetime

from functools import reduce  

from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count

from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product

from app.models import Bug
from app.models import BugReport


"""
  bug: report
"""
@require_http_methods(["GET"])
def report(request):

    today = time.strftime("%Y-%m-%d", time.localtime())
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        req = request.GET
        product_id = req["product_id"]
        t = req["type"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要请求参数"})
    
    # today bug data
    status_data = []
    create = Bug.objects.filter(Q(create_time__gte=today) & Q(product_id=product_id)).\
        aggregate(create=Count("create_time"))
    status_data.append(create)

    closed = Bug.objects.\
        filter(Q(closed_time__gte=today) & Q(status="Closed") & Q(product_id=product_id)).\
        aggregate(closed=Count("closed_time"))
    status_data.append(closed)
    
    fixed = Bug.objects.\
        filter(Q(fixed_time__gte=today) & Q(status="Fixed") & Q(product_id=product_id)).\
        aggregate(hangUp=Count("fixed_time"))
    status_data.append(fixed)

    hangUp = Bug.objects.\
        filter(Q(hangUp_time__gte=today) & Q(status="HangUp") & Q(product_id=product_id)).\
        aggregate(hangUp=Count("hangUp_time"))
    status_data.append(hangUp)

    # surplus no fixed bug
    surplus_bug = Bug.objects.\
        filter(Q(product_id=product_id) & ~Q(status="Closed") & ~Q(status="Fixed")).\
        annotate(name = F("severity__name")).\
        values("name").annotate(value=Count("id")).order_by("-value")

    # 致命一级bug
    fatal_bug = Bug.objects.filter(Q(product_id=product_id) & Q(severity="Fatal")).order_by("id").\
        values("id","title")

    today_data = {
        "datetime": get_time,
        "product_id":product_id,
        "status_data":status_data,
        "surplus_bug":list(surplus_bug),
        "fatal_bug":list(fatal_bug)
    }
    try:
        report = BugReport(
            content = json.dumps(today_data)
        )
        report.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"出现错误了，请联系管理员"})
    else:
        return JsonResponse({"status":20000,"report_id":report.report_id,"msg":"已成功生成今天的缺陷日报"})

"""
  bug: report details
"""
@require_http_methods(["GET"])
def report_details(request):
    try:
        req = request.GET
        report_id = req["report_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"report_id不能为空"})

    try:
        data = BugReport.objects.filter(report_id=report_id).values("content")
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"报告获取失败"})
    else:
        t = list(data)[0]["content"]
        return JsonResponse({"status":20000,"data":t})

