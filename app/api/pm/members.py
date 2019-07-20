#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from functools import wraps

from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import User
from app.models import UserRole
from app.models import Authentication
from app.models import Product
from app.models import ProductMembers
from app.api.auth import get_user_object


curremt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

"""
  项目组成员
"""
@require_http_methods(["GET"])
def members_list(request):

    try:
        product_id = request.GET["product_id"]
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": "因请求中缺少项目ID, 请求中止."})

    if "role" in request.GET:
        role = request.GET["role"]
        data = ProductMembers.objects.\
            filter(
                Q(product_id=product_id) &
                Q(member_id__user_role=role) &
                ~Q(member_id__realname__icontains=u"管理员")).\
            order_by("-user_role").\
            annotate(
                realname = F("member_id__realname"),
                user_id = F("member_id"),
                role=F("user_role"),
                role_name=F("user_role__name")).\
            values("user_id","realname","role_name","status","join_time","banned_time")
    else:
        data = ProductMembers.objects.\
            filter(
                Q(product_id=product_id) &
                ~Q(member_id__realname__icontains=u"管理员")
                ).\
            order_by("-user_role").\
            annotate(
                realname = F("member_id__realname"),
                user_id = F("member_id"),
                role=F("user_role"),
                role_name=F("user_role__name")).\
            values("user_id","realname","role","role_name","status","join_time","banned_time")

    product_data = Product.objects.filter(product_id=product_id).values_list("product_code",flat=True)
    return JsonResponse({"status": 20000, "product_id":product_id,"product_code":product_data[0], "data": list(data)})

"""
  项目组加入成员
"""
@csrf_exempt
@require_http_methods(["POST"])
def product_members_join(request):

    try:
        rep = json.loads(request.body)
        product_id = rep["product_id"]
        user_id = rep["user_id"]
        role = rep["role"]
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求参数."})

    try:
        product_object = Product.objects.get(product_id=product_id)
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": "product_id无效."})

    try:
        role_object = UserRole.objects.get(role=role)
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": "product_id无效."})

    try:
        uid = User.objects.get(user_id=user_id)
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": "user_id无效."})

    is_check = ProductMembers.objects.filter(Q(member_id=user_id) & Q(product_id=product_id))
    if len(is_check) > 0:
        return JsonResponse({"status": 20004, "msg": "此用户已在项目组，请勿重复添加."})

    try:
        data = ProductMembers(
            member_id = uid,
            product_id = product_object,
            status = 0,
            user_role = role_object
            )
        data.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"保存成功"})


"""
  项目组移除成员
"""
@csrf_exempt
@require_http_methods(["POST"])
def product_members_ban(request):

    try:
        rep = json.loads(request.body)
        product_id = rep["product_id"]
        user_id = rep["user_id"]
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": "缺少必要的请求参数."})

    try:
        u = ProductMembers.objects.get(Q(member_id=user_id) & Q(product_id=product_id))
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": "user_id或product_code无效."})

    try:
        u.status = 1
        u.banned_time = curremt_time
        u.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"用户移除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"已将用户从产品中成功移除"})

"""
  项目组重新加入成员
"""
@require_http_methods(["POST"])
@csrf_exempt
def product_members_rejoin(request):

    try:
        rep = json.loads(request.body)
        product_id = rep["product_id"]
        user_id = rep["user_id"]
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求参数."})

    try:
        u = ProductMembers.objects.get(Q(member_id=user_id) & Q(product_id=product_id))
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": "user_id或product_cid无效."})

    try:
        u.status = 0
        u.banned_time = None
        u.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"用户重新加入失败"})
    else:
        return JsonResponse({"status":20000,"msg":"用户重新成功加入此产品"})
