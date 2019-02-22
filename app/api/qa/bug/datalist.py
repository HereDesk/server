#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
import string
from datetime import datetime
 

from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release

from app.models import Bug

from app.api.utils import get_listing
from app.api.auth import get_uid
from app.api.auth import get_prdocut_user_role

# get cureent time
curremt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())


"""
  缺陷list
"""
@csrf_exempt
@require_http_methods(["GET"])
def list(request):

    # query builder
    conditions = Q()
    q1 = Q()
    q1.connector = "AND"
    
    try:
        req = request.GET.dict()
        product_id = req["product_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"请求缺少必要的值"})

    if "release" in req:
        try:
            release = req["release"]
            if release == "all":
                del req["release"]
            else:
                release_query = Release.objects.\
                    filter(Q(product_id=product_id) & Q(version=release)).values('id')
                if len(release_query) == 0:
                    return JsonResponse({"status":40004,"msg":"版本号错误"})
                else:
                    version_id = release_query[0]["id"]
                    q1.children.append(Q(**{"version_id": version_id }))
        except Exception as e:
            return JsonResponse({"status":40004,"msg":"产品名称或版本号错误"})

    if "status" in req:
        if req["status"] == "all":
            del req["status"]
        elif req["status"] == "notClosed":
            q1.children.append(~Q(**{"status":"Closed"}))
        else:
            status = req["status"]
            q1.children.append(Q(**{"status":status}))

    if "m1_id" in request.GET:
        m1_id = request.GET["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))
        
    if "m2_id" in request.GET:
        m2_id = request.GET["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    if "severity" in req:
        if req["severity"] == "all":
            del req["severity"]

    if "priority" in req:
        if req["priority"] == "all":
            del req["priority"]

    for data in req.items():
        if "product_id" in data or "priority" == data[0] or "severity" in data:
            q1.children.append(Q(**{data[0]: data[1]}))

    if "operate" in req:
        operate = req["operate"]
        if operate == "AssignedByMe":
            conditions.children.append(Q(**{"assignedTo_id":get_uid(request)}))
        if operate == "ResolvedByMe":
            conditions.children.append(Q(**{"fixed_id":get_uid(request)}))
        if operate == "ClosedByMe":
            conditions.children.append(Q(**{"closed_id":get_uid(request)}))
        if operate == "CreatedByMe":
            conditions.children.append(Q(**{"creator_id":get_uid(request)}))
        if operate == "notClosed":
            q1.children.append(~Q(**{"status":"Closed"}))
        if operate == "WaitPending":
            product_role = get_prdocut_user_role(request,product_id)
            if product_role == 'test':
                q2 = Q()
                q2.connector = "AND"
                q2.children.append(Q(**{"assignedTo_id":get_uid(request)}))
                q2.children.append(~Q(**{"status":"closed"}))
                conditions.add(q2, "AND")
            else:
                q2 = Q()
                q2.connector = "AND"
                q2.children.append(Q(**{"assignedTo_id":get_uid(request)}))
                temp_q2_1 = Q()
                temp_q2_1.connector = "OR"
                temp_q2_1.children.append(Q(**{"status":"Open"}))
                temp_q2_1.children.append(Q(**{"status":"Reopen"}))
                temp_q2_1.children.append(Q(**{"status":"Hang-up"}))
                q2.add(temp_q2_1, "AND")
                conditions.add(q2, "AND")
        if operate == "NotResolved":
            q2 = Q()
            q2.connector = "OR"
            q2.children.append(Q(**{"status":"New"}))
            q2.children.append(Q(**{"status":"Open"}))
            q2.children.append(Q(**{"status":"Reopen"}))
            q2.children.append(Q(**{"status":"Hang-up"}))
            conditions.add(q2, "AND")

    if "sort" in req and "sort_field" in req:
        if req["sort"] == '-':
            sort = req["sort"] + req["sort_field"]
        else:
            sort = req["sort_field"]
    else:
        sort = "-create_time"
            
    conditions.add(q1, "AND")

    try:
        print(conditions)
        data = Bug.objects.filter(conditions).\
            annotate(
                creator_user=F("creator_id__realname"),
                assignedTo_user=F("assignedTo_id__realname"),
                fixed_user=F("fixed_id__realname"),
                last_operation_user=F("last_operation__realname"),
                severity_name=F("severity__name"),
                priority_name=F("priority__name"),
                status_name = F("status__name"),
                solution_name=F("solution__name"),
                product_code=F("product_id__product_code")
            ).\
            order_by(sort).\
            values("id","product_id","product_code",
                "bug_id","title","status","status_name","solution_name",\
                "priority","priority_name","severity","severity_name","solution",\
                "creator_id","creator_user","create_time",\
                "assignedTo_user","assignedTo_time",
                "fixed_id","fixed_time","fixed_user",
                "closed_id","closed_time","last_time","last_operation_user")
    except Exception as e:
        print(e)
        return JsonResponse({"status":40004,"msg":"异常错误，请联系管理员"})
    else:
        return HttpResponse(get_listing(request.GET, data))
