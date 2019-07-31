#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from datetime import datetime

from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release

from app.models import Bug
from app.models import BugAnnex
from app.models import BugHistory

"""
 bug details
"""
@require_http_methods(["GET"])
def details(request):
    try:
        bug_id = request.GET["bug_id"]
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"请求参数错误."})

    data = Bug.objects.filter(bug_id=bug_id).\
        annotate(
            product_code=F("product_id__product_code"),
            creator_user=F("creator_id__realname"),
            assignedTo_user=F("assignedTo_id__realname"),
            fixed_user=F("fixed_id__realname"),
            closed_user=F("closed_id__realname"),
            severity_name=F("severity__name"),
            priority_name=F("priority__name"),
            status_name=F("status__name"),
            solution_name=F("solution__name"),
            release=F("version_id__version"),
            bug_type_name=F("bug_type__name"),
            bug_source_name=F("bug_source__name"),
            m1_name=F("m1_id__m1_name"),
            m2_name=F("m2_id__m2_name"),
            last_operation_user=F("last_operation__realname")
        ).\
        values("id","product_id","product_code","release","bug_id","case_id",\
            "m1_name","m2_name","m1_id","m2_id",\
            "title","steps","reality_result","expected_result","remark",\
            "priority","priority_name","severity","severity_name",\
            "bug_type","bug_type_name","solution","solution_name","status","status_name",\
            "bug_source","bug_source_name",\
            "creator_id","creator_user","create_time",\
            "assignedTo_id","assignedTo_user","assignedTo_time",\
            "fixed_user","fixed_id","fixed_time",\
            "closed_user","closed_id","closed_time","last_time","last_operation_user","bug_label")

    annex = BugAnnex.objects.filter(Q(bug_id=bug_id) & Q(is_delete=0)).values("url")

    annex_tmp = []
    for ax in annex:
        try:
            ax["suffix"] = str(ax["url"]).split('.')[-1]
        except Exception as e:
            ax["suffix"] = "unknow"
        annex_tmp.append(ax)
    
    if len(data) == 0:
        return JsonResponse({"status":20004,"msg":"没找到数据"})
    else:
        return JsonResponse({
            "status":20000,
            "data":list(data)[0],
            "annex":list(annex_tmp)
        })

"""
  bug history
"""
def history(request):
    try:
        bug_id = request.GET["bug_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"BugId不能为空"})

    data = BugHistory.objects.filter(bug_id=bug_id).\
        annotate(
            username = F("user_id__realname")
            ).\
        order_by("create_time").\
        values("record_id","user_id","bug_id","username","desc","remark_status","remark","create_time")

    return JsonResponse({"status":20000,"data":list(data)})
