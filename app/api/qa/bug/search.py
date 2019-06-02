#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from datetime import datetime
from datetime import datetime,timedelta

import operator
from functools import reduce  

from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release
from app.models import ProductMembers

from app.models import Bug

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_uid

"""
  bug search
"""
def handle_search(data):
    sdata = data["SearchType"]
    symbol = data["Operators"]
    wd = data["wd"]
    query = Q()
    if symbol == "like":
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
            date_range = wd.split("#")
            date_range[1] = datetime.strptime(date_range[1], "%Y-%m-%d") + timedelta(days = 1)
            query.children.append(Q(**{field:date_range}))

        print(query)
    return query




"""
  bug search
"""
def handle_advanced_search(req):
    conditions = Q()

    status_query = Q()
    priority_query = Q()
    severity_query = Q()
    creator_query = Q()
    fixed_user_query = Q()
    assignedTo_user_query = Q()
    closed_user_query = Q()
    if "status_list" in req:
        status_list = req["status_list"]
        if status_list:
            status_query.children.append(Q(**{"status__key__in":status_list}))
            conditions.add(status_query, "AND")

    if "priority_list" in req:
        priority_list = req["priority_list"]
        if priority_list:
            print(priority_list)
            priority_query.children.append(Q(**{"priority__key__in":priority_list}))
            conditions.add(priority_query, "AND")

    if "severity_list" in req:
        severity_list = req["severity_list"]
        if severity_list:
            severity_query.children.append(Q(**{"severity__key__in":severity_list}))
            conditions.add(severity_query, "AND")

    if "creator" in req:
        creator = req["creator"]
        if creator:
            creator_list = creator.split(" ")
            creator_query.children.append(Q(**{"creator_id__realname__in":creator_list}))
            conditions.add(creator_query, "AND")

    if "fixed_user" in req:
        fixed_user = req["fixed_user"]
        if creator:
            fixed_user_list = creator.split(" ")
            fixed_user_query.children.append(Q(**{"fixed_id__realname__in":fixed_user_list}))
            conditions.add(fixed_user_query, "AND")

    
    if "assignedTo_user" in req:
        assignedTo_user = req["assignedTo_user"]
        if assignedTo_user:
            assignedTo_user_list = assignedTo_user.split(" ")
            assignedTo_user_query.children.append(Q(**{"assignedTo_id__realname__in":assignedTo_user_list}))
            conditions.add(assignedTo_user_query, "AND")

    if "closed_user" in req:
        closed_user = req["closed_user"]
        if closed_user:
            closed_user_list = closed_user.split(" ")
            closed_user_query.children.append(Q(**{"closed_id__realname__in":closed_user_list}))
            conditions.add(closed_user_query, "AND")

    if "create_time" in req:
        create_time = req["create_time"]
        if isinstance(create_time,list) and len(create_time) == 2:
            date_range = req["create_time"]
            date_range[1] = datetime.strptime(date_range[1], "%Y-%m-%d") + timedelta(days = 1)
            conditions.children.append(Q(**{"create_time__range": date_range}))

    if "closed_time" in req:
        closed_time = req["closed_time"]
        if isinstance(create_time,list) and len(closed_time) == 2:
            date_range = req["closed_time"]
            date_range[1] = datetime.strptime(date_range[1], "%Y-%m-%d") + timedelta(days = 1)
            conditions.children.append(Q(**{"closed_time__range": date_range}))

    if "assignedTo_time" in req:
        assignedTo_time = req["assignedTo_time"]
        if isinstance(assignedTo_time,list) and len(assignedTo_time) == 2:
            date_range = req["create_time"]
            date_range[1] = datetime.strptime(date_range[1], "%Y-%m-%d") + timedelta(days = 1)
            conditions.children.append(Q(**{"assignedTo_time__range": date_range}))

    if "fixed_time" in req:
        fixed_time = req["fixed_time"]
        if isinstance(fixed_time,list) and len(fixed_time) == 2:
            date_range = req["fixed_time"]
            date_range[1] = datetime.strptime(date_range[1], "%Y-%m-%d") + timedelta(days = 1)
            conditions.children.append(Q(**{"fixed_time__range": date_range}))

    return conditions




@csrf_exempt
@require_http_methods(["POST"])
def search(request):

    query = Q()
    query.connector = "AND"

    # check value
    try:
        req = json.loads(request.body)
        advanced_search = req["isShowAdSearch"]
        product_id = req["product_id"]
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"请求缺少必要的值."})

    # check product code
    try:
        query.children.append(Q(**{"product_id":product_id}))
        productObject = Product.objects.get(product_id=product_id)
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"查询产品异常."})

    # check version
    if "release" in req:
        try:
            release = req["release"]
            if release == "all":
                del req["release"]
            else:
                release_query = Release.objects.\
                    filter(Q(product_id=product_id) & Q(version=release)).values('id')
                if len(release_query) == 0:
                    return JsonResponse({"status":40001,"msg":"版本号错误"})
                else:
                    query.children.append(Q(**{"version_id":list(release_query)[0]['id']}))
        except Exception as e:
            return JsonResponse({"status":40001,"msg":"产品名称或版本号错误"})
    
    # get sort field
    if "sort" in req and "sort_field" in req:
        sort = req["sort"] + req["sort_field"]
    else:
        sort = "create_time"
        
    query.children.append(Q(**{"isDelete":0}))

    # simple search
    try:
        wd = req["wd"]
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"请求缺少必要的值."})

    if wd.isdigit():
        query.children.append(Q(**{"id__icontains":wd}))
    else:
        developer_list = ProductMembers.objects.\
            filter(Q(product_id=product_id) & Q(role="developer")).\
            annotate(realname = F("member_id__realname")).\
            values("realname")
        developer_list = [ i["realname"] for i in developer_list ]
        if wd in developer_list:
            query.children.append(Q(**{"assignedTo_id__realname__icontains":wd}))
        else:
            query.children.append(Q(**{"title__icontains":wd}))

    if "status" in req:
        if req["status"] == "all":
            del req["status"]
        elif req["status"] == "notClosed":
            query.children.append(~Q(**{"status":"Closed"}))
        else:
            status = req["status"]
            query.children.append(Q(**{"status":status}))

    # advanced search
    # if advanced_search == "yes":
    #     advanced_query = handle_advanced_search(req)
    #     query.add(advanced_query,"AND")

    try:
        data = Bug.objects.filter(query). \
            annotate(
                creator_user=F("creator_id__realname"),
                assignedTo_user=F("assignedTo_id__realname"),
                severity_name=F("severity__name"),
                priority_name=F("priority__name"),
                status_name = F("status__name"),
                solution_name=F("solution__name"),
                last_operation_user=F("last_operation__realname")
            ).\
            order_by(sort).\
            values("id","bug_id","title","status","status_name","solution_name",\
            "priority","priority_name","severity","severity_name","solution",\
            "creator_id","creator_user","create_time",\
            "assignedTo_user","assignedTo_time","fixed_id","fixed_time","closed_id","closed_time",\
            "last_operation_user","last_time")
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": u"异常错误，请联系管理员."})
    else:
        if len(data) == 0:
            return JsonResponse({"status": 20004, "msg": "没有查到该条数据"})
        else:
            return HttpResponse(get_listing(req,data))