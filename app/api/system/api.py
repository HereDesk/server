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
from app.models import Api
from app.models import ApiPermissions

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_user_name
from app.api.auth import get_uid

"""
    权限列表
"""
@csrf_exempt
@require_http_methods(["GET"])
def api_list(request):
    try:
        group = request.GET["group"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"参数错误"})

    try:
        tmp_data = []
        api_list = Api.objects.all().values("id","api_name","url","flag")
        perm_data = ApiPermissions.objects.filter(Q(group=group)).values("api_id","is_allow")
        for pl in api_list:
            pl["is_allow"] = 0
            tmp_data.append(pl)
        if len(perm_data) > 0:
            for i1 in perm_data:
                for i2 in tmp_data:
                    if i1["api_id"] == i2["id"]:
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
    增加权限
"""
@csrf_exempt
@require_http_methods(["POST"])
def api_create(request):
    try:
        req = json.loads(request.body)
        name = req["api_name"]
        code = req["api_code"]
        url = req["url"]
        flag = req["flag"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"缺少参数"})

    try:
        p = Api(
            api_name = name,
            url = url,
            api_code = code,
            flag = flag
            )
        p.save()
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"服务器开小差了"})
    else:
        return JsonResponse({"status":20000,"msg":"增加api成功"})

"""
  管理权限
"""
@csrf_exempt
@require_http_methods(["POST"])
def api_manage(request):
    try:
        req = json.loads(request.body)
        api_id = req['api_id']
        group = req['group']
        is_allow = req['is_allow']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少参数"})

    try:
        is_check_data = ApiPermissions.objects.filter(Q(api_id=api_id) & Q(group=group)).values('id')
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"服务器开小差了"})
    if len(is_check_data) == 0:
        try:
            pg = ApiPermissions(
                api_id = Api.objects.get(id=api_id),
                group = Group.objects.get(group=group),
                is_allow = is_allow
                )
            pg.save()
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"保存失败"})
        else:
            return JsonResponse({"status":20000,"msg":"保存成功"})
    else:
        data_id = list(is_check_data)[0]["id"]
        try:
            p = ApiPermissions.objects.get(id=data_id)
            p.is_allow = is_allow
            p.save()
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"保存失败"})
        else:
            return JsonResponse({"status":20000,"msg":"保存成功"})
        
