#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from datetime import datetime

import operator
from functools import reduce  

from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count

from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release
from app.models import ModuleA
from app.models import User

from app.models import BugType
from app.models import BugStatus
from app.models import BugPriority
from app.models import BugSeverity
from app.models import Bug
from app.models import BugAnnex
from app.models import BugHistory
from app.models import BugSolution

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_user_name
from app.api.auth import get_uid

"""
  bug search
"""
def handle_search(data):
    sdata = data["SearchType"]
    symbol = data["Operators"]
    wd = data["wd"]
    query = Q()
    if symbol == "=":
        query.connector = "OR"
        if "ID" in sdata:
            query.children.append(Q(**{"id__icontains":wd}))
        if "title" in sdata:
            query.children.append(Q(**{"title__icontains":wd}))
        if "priority" in sdata:
            query.children.append(Q(**{"priority__name__icontains":wd}))
        if "severity" in sdata:
            query.children.append(Q(**{"severity__name__icontains":wd}))
        if "bug_type" in sdata:
            query.children.append(Q(**{"bug_type__name__icontains":wd}))
        if "user" in sdata:
            uid_list = User.objects.filter(realname__icontains=wd).values_list("user_id",flat=True)
            field = ""
            if "fixed" in sdata:
                field = "fixed_id"
            if "creator" in sdata:
                field = "creator_id"
            if "closed" in sdata:
                field = "closed_id"
            if "assignedTo" in sdata:
                field = "assignedTo_id"
            for i in uid_list:
                query.children.append(Q(**{field:i}))
        if "time" in sdata:
            field = ""
            if "create" in sdata:
                field = "create_time__contains"
            if "fixed" in sdata:
                field = "fixed_time__contains"
            if "closed" in sdata:
                field = "closed_time__contains"
            query.children.append(Q(**{field:wd}))
    if symbol == "!=":
        query.connector = "OR"
        if "ID" in sdata:
            query.children.append(~Q(**{"id__icontains":wd}))
        if "title" in sdata:
            query.children.append(~Q(**{"title__icontains":wd}))
        if "priority" in sdata:
            query.children.append(~Q(**{"priority__name__icontains":wd}))
        if "severity" in sdata:
            query.children.append(~Q(**{"severity__name__icontains":wd}))
        if "bug_type" in sdata:
            query.children.append(~Q(**{"bug_type__name__icontains":wd}))
        if "user" in sdata:
            uid_list = User.objects.filter(~Q(realname__icontains=wd)).values_list("user_id",flat=True)
            field = ""
            if "fixed" in sdata:
                field = "fixed_id"
            if "creator" in sdata:
                field = "creator_id"
            if "closed" in sdata:
                field = "closed_id"
            if "assignedTo" in sdata:
                field = "assignedTo_id"
            for i in uid_list:
                query.children.append(~Q(**{field:i}))
        if "time" in sdata:
            field = ""
            if "create" in sdata:
                field = "create_time__contains"
            if "fixed" in sdata:
                field = "fixed_time__contains"
            if "closed" in sdata:
                field = "closed_time__contains"
            query.children.append(~Q(**{field:wd}))

    if symbol != "!=" and symbol != "=" and "time" in sdata:
        field = ""
        if symbol == ">=":
            if "create" in sdata:
                field = "create_time__gte"
            if "fixed" in sdata:
                field = "fixed_time__gte"
            if "closed" in sdata:
                field = "closed_time__gte"
            query.children.append(Q(**{field:wd}))
        if symbol == ">":
            if "create" in sdata:
                field = "create_time__gt"
            if "fixed" in sdata:
                field = "fixed_time__gt"
            if "closed" in sdata:
                field = "closed_time__gt"
            query.children.append(Q(**{field:wd}))
        if symbol == "<=":
            if "create" in sdata:
                field = "create_time__lte"
            if "fixed" in sdata:
                field = "fixed_time__lte"
            if "closed" in sdata:
                field = "closed_time__lte"
            query.children.append(Q(**{field:wd}))
        if symbol == "<":
            if "create" in sdata:
                field = "create_time__lt"
            if "fixed" in sdata:
                field = "fixed_time__lt"
            if "closed" in sdata:
                field = "closed_time__lt"
            query.children.append(Q(**{field:wd}))
        if symbol == "range":
            if "create" in sdata:
                field = "create_time__range"
            if "fixed" in sdata:
                field = "fixed_time__range"
            if "closed" in sdata:
                field = "closed_time_range"
            query.children.append(Q(**{field:wd}))
    return query
    
@csrf_exempt
@require_http_methods(["POST"])
def search(request):

    q1 = Q()
    q2 = Q()
    q1.connector = "AND"

    try:
        req = json.loads(request.body)
        product_code = req["product_code"]
        Operators = req["Operators"]
        SearchType = req["SearchType"]
        wd = req["wd"]
        q1.children.append(Q(**{"product_code":"product_code"}))
        productObject = Product.objects.get(product_code=product_code)
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"请求缺少必要的值."})

    if "release" in req:
        release = req["release"]
        try:
            release = req["release"]
            if release == "all":
                del req["release"]
            else:
                req["version_id"] = Release.objects.get(Q(product_code=product_code) & Q(version=release))
                del req["release"]
        except Exception as e:
            return JsonResponse({"status":40001,"msg":"产品名称或版本号错误"})

    if "status" in req:
        if req["status"] == "all":
            del req["status"]
        elif req["status"] == "notClosed":
            q1.children.append(~Q(**{"status":"Closed"}))
        else:
            status = req["status"]
            q1.children.append(Q(**{"status":status}))

    try:
        q1.children.append(Q(**{"isDelete":0}))
        q1.add(handle_search(req), "OR")
        data = Bug.objects.filter(q1). \
            annotate(
                creator_user=F("creator_id__realname"),
                assignedTo_user=F("assignedTo_id__realname"),
                severity_name=F("severity__name"),
                priority_name=F("priority__name"),
                status_name = F("status__name"),
                solution_name=F("solution__name")
            ).\
            order_by("-create_time").\
            values("id","bug_id","title","status","status_name","solution_name",\
            "priority","priority_name","severity","severity_name","solution",\
            "creator_id","creator_user","create_time",\
            "assignedTo_user","assignedTo_time","fixed_id","fixed_time","closed_id","closed_time")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 40004, "msg": u"异常错误，请联系管理员."})
    else:
        if len(data) == 0:
            return JsonResponse({"status": 20004, "msg": "没有查到该条数据"})
        else:
            return HttpResponse(get_listing(req,data))