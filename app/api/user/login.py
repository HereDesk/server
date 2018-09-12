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

from app.api.gpd import p_encrypt
"""
 10000:register success
 10004:未知异常
 10050:密码或用户名错误
 10051:密码或用户名长度错误
 10052:该邮箱已被人使用
"""

"""
 登录接口（使用电子邮件注册）
"""
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    try:
        req_info = json.loads(request.body)
        username = req_info["username"]
        password = req_info["password"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"请求缺少必要的值."})

    try:
        if '@' in username:
            pass
        else:
            return JsonResponse({"status": 10004, "msg": u"不是有效的用户名。"})
        is_check_status = User.objects.filter(Q(email=username)).values_list('user_status')
        if (is_check_status[0][0]) == 2:
            return JsonResponse({"status": 14401, "msg": u"账号已被封禁或注销，请联系管理员"})
    except Exception as e:
        return JsonResponse({"status":10004,"msg":u"用户名或密码错误。"})

    user_info = User.objects.filter(email=username).values_list("user_id","password")
    if user_info:
        q_uid = user_info[0][0]
        q_passwd = user_info[0][1]
        
        try:
            # 密码校验
            p = p_encrypt(password,username)
        except Exception as e:
            return JsonResponse({"status":40000,"msg":u"系统出错,请联系管理员"})

        if p == q_passwd:
            ut = Authentication.objects.filter(uid=q_uid).\
                annotate(
                    group=F('uid__group__group'),
                    realname=F('uid__realname')
                    ).\
                values("token","uid","group","realname")
            return JsonResponse({"status": 10000, "msg": u"恭喜您！登录成功", "data": list(ut)})
        else:
            return JsonResponse({"status": 10004, "msg": u"用户名或密码错误。"})
    else:
        return JsonResponse({"status": 10004, "msg": u"用户名不存在。"})
