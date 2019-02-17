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

from app.models import Authentication
from app.models import User
from app.models import Group
from app.models import Pages
from app.models import PagesPermissions

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_user_name
from app.api.auth import get_uid
from app.api.auth import is_admin

"""
    权限列表
"""
@csrf_exempt
@require_http_methods(["GET"])
def pages_list(request):
    try:
        group = request.GET["group"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"参数错误"})

    try:
        tmp_data = []
        pages_list = Pages.objects.all().\
            values("id","page_name","page_url","flag","desc").\
            order_by("page_name")
        perm_data = PagesPermissions.objects.filter(Q(group=group)).values("page_id","is_allow")
        for pl in pages_list:
            pl["is_allow"] = 0
            tmp_data.append(pl)
        if len(perm_data) > 0:
            for i1 in perm_data:
                for i2 in tmp_data:
                    if i1["page_id"] == i2["id"]:
                        i2["is_allow"] = i1["is_allow"]

        flag_data = list(set([ i1["flag"] for i1 in tmp_data ]))
        data = [ {"flag":i,"data":[]} for i in flag_data ]
        for i1 in tmp_data:
            for i2 in data:
                if i1["flag"] == i2["flag"]:
                    i2["data"].append(i1)
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"没查到数据"})
    else:
        return JsonResponse({"status":20000,"data":list(data)})

"""
    增加页面
"""
@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    try:
        req = json.loads(request.body)
        page_name = req["page_name"]
        page_url = req["page_url"]
        flag = req["flag"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"缺少参数"})

    try:
        p = page(
            page_name = page_name,
            page_url = page_url,
            flag = flag
            )
        p.save()
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"服务器开小差了"})
    else:
        return JsonResponse({"status":20000,"msg":"增加路由成功"})

"""
  管理权限
"""
@csrf_exempt
@require_http_methods(["POST"])
def manage(request):
    try:
        req = json.loads(request.body)
        page_id = req['page_id']
        group = req['group']
        is_allow = req['is_allow']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少参数"})

    try:
        is_check = PagesPermissions.objects.filter(Q(page_id=page_id) & Q(group=group)).values('id')
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"服务器开小差了"})
    if len(is_check) == 0:
        try:
            pg = PagesPermissions(
                page_id = Pages.objects.get(id=page_id),
                group = Group.objects.get(group=group),
                is_allow = is_allow
                )
            pg.save()
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"保存失败"})
        else:
            return JsonResponse({"status":20000,"msg":"保存成功"})
    else:
        data_id = list(is_check)[0]["id"]
        try:
            p = PagesPermissions.objects.get(id=data_id)
            p.is_allow = is_allow
            p.save()
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"保存失败"})
        else:
            return JsonResponse({"status":20000,"msg":"保存成功"})
        
