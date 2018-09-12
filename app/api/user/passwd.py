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
from django.db.models import Count
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import User
from app.models import Authentication

from app.api.gpd import p_encrypt
from app.api.gpd import generate_token
from app.api.auth import get_user_object
from app.api.auth import get_uid
from app.api.auth import _auth

"""
  修改密码
"""
@csrf_exempt
@require_http_methods(["POST"])
def set_passwd(request):

    try:
        req_info = json.loads(request.body)
        old_passwd = req_info["oldPassword"]
        new_passwd = req_info["newPassword"]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"缺少必要的请求值."})

    try:
        userinfo = User.objects.filter(user_id=get_uid(request)).values_list('password','email')
        # 旧密码加密后的字符串
        old_passwd_encrypted = p_encrypt(str(old_passwd),userinfo[0][1])
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"系统异常错误."})
    else:
        # 旧密码校验
        if old_passwd_encrypted != userinfo[0][0]:
            return JsonResponse({"status":20004,"msg":"旧密码输入错误"})
        
    if len(new_passwd) < 8:
        return JsonResponse({"status":20004,"msg":"新密码长度太短"})
    else:
        # 密码加密
        encrypt_passwd = p_encrypt(str(new_passwd),userinfo[0][1])
        try:
            pd = User.objects.get(user_id=get_uid(request))
            pd.password = encrypt_passwd
            pd.save()
        except Exception as e:
            return JsonResponse({"status":20004,"mgs":"密码修改失败"})
        # token
        try:
            tk = Authentication.objects.get(uid=get_uid(request))
            tk.token = generate_token()
            tk.save()
        except Exception as e:
            return JsonResponse({"status":40004,"mgs":"密码修改失败"})
        else:
            return JsonResponse({"status":20000,"mgs":"您已成功修改密码，请牢记。"})

"""
  管理员重置其它用户密码
"""
@csrf_exempt
@require_http_methods(['POST'])
def reset_passwd(request):
    try:
        req = json.loads(request.body)
        passwd = req['passwd']
        user_id = req['user_id']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"密码不能为空哦"})

    data = User.objects.filter(user_id=user_id).values_list('email')
    if len(data) == 0:
        return JsonResponse({"status":40004,"msg":"用户不存在"})

    if len(passwd) < 8 or len(passwd) > 16:
        return JsonResponse({"status":20004,"msg":"密码的有效长度为8-16位"})

    # 密码加密
    encrypt_passwd = p_encrypt(str(passwd),data[0][0])
    try:
        # 修改密码
        pd = User.objects.get(user_id=user_id)
        pd.password = encrypt_passwd
        pd.save()

        # token
        tk = Authentication.objects.get(uid=user_id)
        tk.token = generate_token()
        tk.save()
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"密码重置失败"})
    else:
        return JsonResponse({"status":20000,"msg":"密码重置成功。"})










