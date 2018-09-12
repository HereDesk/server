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
from app.models import Permissions
from app.models import PermissionsGroup

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_user_name
from app.api.auth import get_uid

"""
    权限列表
"""
@csrf_exempt
@require_http_methods(["GET"])
def permissions_list(request):
    try:
        group = request.GET["group"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"参数错误"})

    try:
        data = []
        permissions_flag = Permissions.objects.all().values("flag").distinct()
        permissions_list = PermissionsGroup.objects.filter(Q(group=group)).\
            annotate(
                flag=F("permissions_id__flag"),
                name=F("permissions_id__name")
                ).\
            values("permissions_id","is_allow","flag","name")
        for i in permissions_flag:
            temp = []
            for perm in permissions_list:
                if perm["flag"] == i["flag"]:
                    temp.append(perm)
                i["data"] = temp
            data.append(i)
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"没查到数据"})
    else:
        return JsonResponse({"status":20000,"data":data})

"""
    增加权限
"""
@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    try:
        req = json.loads(request.body)
        name = req["name"]
        code = req["code"]
        url = req["url"]
        flag = req["flag"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"缺少参数"})

    try:
        p = Permissions(
            name = name,
            url = url,
            code = code,
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
        permissions_id = req['permissions_id']
        group = req['group']
        is_allow = req['is_allow']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少参数"})

    try:
        is_check = PermissionsGroup.objects.filter(Q(permissions_id=permissions_id) & Q(group=group)).values('id')
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"服务器开小差了"})
    print(is_check)
    if len(is_check) == 0:
        try:
            pg = PermissionsGroup(
                permissions_id = Permissions.objects.get(id=permissions_id),
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
            p = PermissionsGroup.objects.get(id=data_id)
            p.is_allow = is_allow
            p.save()
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"保存失败"})
        else:
            return JsonResponse({"status":20000,"msg":"保存成功"})
        
