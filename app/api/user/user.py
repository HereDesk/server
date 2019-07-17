#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import json
import base64
import requests
from django.http import QueryDict
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import User
from app.models import Authentication
from app.models import UserRole

from app.models import SystemConfig
from app.models import UserConfig

from app.api.gpd import p_encrypt
from app.api.gpd import generate_token

from app.api.auth import get_uid

"""
  用户信息
"""
@csrf_exempt
@require_http_methods(["GET"])
def userinfo(request):
    uid = get_uid(request)
    data = User.objects.\
        filter(user_id=uid).\
        values('user_id','realname',"username","identity","email")
    query_cfg = UserConfig.objects.\
        filter(Q(user_id=uid)).\
        values("code","code_value")
    config = {}
    for i in query_cfg:
        config.update({i["code"]:i["code_value"]}) 
    return JsonResponse({"status":20000,"data":data[0],"config":config})
    
"""
  用户列表
"""
@require_http_methods(["GET"])
def user_list(request):
    data = User.objects.\
        filter(~Q(realname="超级管理员")).\
        values('user_id','email','identity','realname','user_status','position',\
            'create_time','update_time')
    return JsonResponse({"status":20000,"data":list(data)})

"""
  群组
"""
@require_http_methods(["GET"])
def group(request):
    data = UserRole.objects.\
        filter(~Q(role="admin")).\
        values('group','name')
    return JsonResponse({"status":20000,"data":list(data)})


"""
  用户封禁操作
"""
@csrf_exempt
@require_http_methods(['POST'])
def banned(request):
    # 封禁权限检测
    uid = get_uid(request)
    is_check_admin = User.objects.filter(Q(user_id=uid) & Q(user_status='1'))
    if len(is_check_admin) == 0:
        return JsonResponse({"status":14444,"msg":"您不是管理员，不能进行此项操作"})
    
    try:
        req_info = json.loads(request.body)
        user_id = req_info["user_id"]
        code = req_info["code"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"请求缺少必要的值."})
    
    # 用户检测
    is_check_banned = User.objects.filter(Q(user_id=user_id)).values_list('user_status')
    if len(is_check_banned) == 1:
        pass
        banned_user_status = is_check_banned[0][0]
    else:
        return JsonResponse({"status":10005,"msg":"用户不存在"})

    if code == "2":
        try:
            bd = User.objects.get(user_id=user_id)
            bd.user_status = 2
            bd.save()
        except Exception as e:
            return JsonResponse({"status":10061,"msg":"封禁失败"})
        else:
            return JsonResponse({"status":10060,"msg":"封禁成功"})
    elif code == '1':
        try:
            bd = User.objects.get(user_id=user_id)
            bd.user_status = 1
            bd.save()
        except Exception as e:
            return JsonResponse({"status":10061,"msg":"解封失败"})
        else:
            return JsonResponse({"status":10060,"msg":"解封成功"})
    else:
        return JsonResponse({"status":40004,"msg":"异常错误"})

"""
  用户增加
"""
@csrf_exempt
@require_http_methods(['POST'])
def add(request):

    position_list = [
        'manager','developer','test','android','ios','server','web/H5','pm','design','other'
        ]
    try:
        req_info = json.loads(request.body)
        email = req_info["email"]
        password = req_info["password"]
        realname = req_info["realname"]
        position = req_info["position"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"缺少必要的请求值."})
    else:
        if len(email) < 8 or len(email) > 30:
            return JsonResponse({"status":20004,"msg":"Email的有效长度为8到30位."})
        if len(password) < 6 or len(password) > 16:
            return JsonResponse({"status":20004,"msg":"Email的有效长度为6到16位."})
        if len(realname) < 2 or len(realname) > 8:
            return JsonResponse({"status":20004,"msg":"真实姓名的有效长度为2到8位."})
        if position not in position_list:
            return JsonResponse({"status":20004, "msg":"岗位/职位信息无效"})

    n = User.objects.filter(email=email).count()
    if n > 0:
        return JsonResponse({"status":40004,"msg":email + "已被使用"})
        
    r = User.objects.filter(realname=realname).count()
    if r > 0:
        return JsonResponse({"status":40004,"msg":realname + "已被使用"})

    try:
        encrypt_passwd = p_encrypt(password,email)
        create_user = User(
            password=encrypt_passwd,
            email=email,
            user_status=1,
            realname=realname,
            identity=1,
            position=position)
        create_user.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"用户创建失败"})
    else:
        uid = create_user.user_id

    try:
        # 生成token
        token = generate_token()
        ud = User.objects.get(user_id=uid)
        auth = Authentication(uid=ud,token=token)
        auth.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"用户创建失败"})
    else:
        return JsonResponse({"status":20000,"msg":"用户创建成功"})
