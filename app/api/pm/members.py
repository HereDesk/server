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
from app.models import Authentication
from app.models import Product
from app.models import ProductMembers
from app.api.auth import get_user_object
from app.api.auth import _auth

curremt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

"""
  项目组成员
"""
@require_http_methods(["GET"])
def product_members(request):
    
    try:
        product_code = request.GET['product_code']
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": "缺少必要的product_code."})

    if 'group' in request.GET:
        group = request.GET['group']
        data = ProductMembers.objects.\
            filter(
                Q(product_code=product_code) & 
                Q(member_id__group=group) & 
                ~Q(member_id__realname__icontains=u"管理员")).\
            order_by('-group').\
            annotate(
                realname = F('member_id__realname'),
                user_id = F('member_id'),
                group = F('member_id__group'),
                position=F('member_id__position')).\
            values('user_id','realname','group','status','join_time','banned_time','position')
    else:
        data = ProductMembers.objects.\
            filter(
                Q(product_code=product_code) & 
                ~Q(member_id__realname__icontains=u"管理员")
                ).\
            order_by('-group').\
            annotate(
                realname = F('member_id__realname'),
                user_id = F('member_id'),
                group = F('member_id__group'),
                position=F('member_id__position')).\
            values('user_id','realname','group','status','join_time','banned_time','position')

    
    return JsonResponse({"status": 20000, "product_code":product_code,"data": list(data)})

"""
  项目组加入成员
"""
@csrf_exempt
@require_http_methods(["POST"])
def product_members_join(request):
    
    try:
        rep = json.loads(request.body)
        product_code = rep['product_code']
        user_id = rep['user_id']
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求参数."})

    try:
        pcode_object = Product.objects.get(product_code=product_code)
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": "product_code无效."})

    try:
        uid = User.objects.get(user_id=user_id)
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": "user_id无效."})

    is_check = ProductMembers.objects.filter(Q(member_id=user_id) & Q(product_code=product_code))
    if len(is_check) > 0:
        return JsonResponse({"status": 20004, "msg": "此用户已在项目组，请勿重复添加."})

    try:
        data = ProductMembers(
            member_id = uid,
            product_code = pcode_object,
            status = 0
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
        product_code = rep['product_code']
        user_id = rep['user_id']
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": "缺少必要的请求参数."})

    try:
        u = ProductMembers.objects.get(Q(member_id=user_id) & Q(product_code=product_code))
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
        product_code = rep['product_code']
        user_id = rep['user_id']
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求参数."})

    try:
        u = ProductMembers.objects.get(Q(member_id=user_id) & Q(product_code=product_code))
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": "user_id或product_code无效."})

    try:
        u.status = 0
        u.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"用户重新加入失败"})
    else:
        return JsonResponse({"status":20000,"msg":"用户重新成功加入此产品"})