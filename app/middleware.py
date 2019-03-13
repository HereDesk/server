#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import time
import datetime
import json
import uuid
import base64
import requests
from django.http import QueryDict
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.db.models import Q
from django.db.models import F
from django.db.models import Count
from django.db.models import Sum

from app.models import User
from app.models import Authentication
from app.models import ProductMembers
from app.models import LoggedLog
from app.models import UserLog

from app.models import Api
from app.models import ApiPermissions

from app.api.auth import get_user_object

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

current_date = datetime.date.today().strftime("%Y-%m-%d")

# 获取agent
def get_user_agent(user_agent):
    platform = ""
    browser = ""
    try:
        if "Macintosh" in user_agent:
            platform = "Mac"
            try:
                browser = user_agent.split(" ")[11].replace("Version", "Safari")
            except Exception as e:
                pass
                browser = "unknown"
        if "iPhone" in user_agent:
            platform = "iPhone"
            try:
                browser = user_agent.split(" ")[14].replace("Version", "Safari")
            except Exception as e:
                pass
                browser = "unknown"
        if "iPad" in user_agent:
            platform = "iPad"
            try:
                browser = user_agent.split(" ")[14].replace("Version", "Safari")
            except Exception as e:
                pass
                browser = "unknown"
        if "Android" in user_agent:
            platform = "Android"
            try:
                browser = user_agent.split(" ")[11]
            except Exception as e:
                pass
                browser = "unknown"
        if "Windows" in user_agent:
            platform = "Windows"
            if "Firefox" in user_agent:
                browser = "Firefox"
            else:
                browser = "unknow"
    except Exception as e:
        platform, browser = "other", "other"
    else:
        return platform,browser



# check user identity
class CheckUserIdentity(MiddlewareMixin):

    def process_request(self, request):

        """
            1. get request info: 
                1) method
                2) ip
                3) user_agent
                4) platform
                5) browser
                6) path
            2. user info:
                1) token
                2) produt_code
        """

        # request method
        method = request.method
        self.product_id = ""
        if method == "GET":
            request_content = request.META["QUERY_STRING"]
            if "product_id" in request.GET:
                self.product_id = request.GET["product_id"]
        elif method == "POST":
            if request.path == "/api/support/upload":
                pass
            else:
                try:
                    request_content = json.loads(request.body)
                    if "product_id" in request_content:
                       self.product_id = request_content["product_id"]
                except Exception as e:
                    print(e)
                    return JsonResponse({"status":14404,"msg":"POST请求不能为空、且请求必须为json"})
        else:
            return JsonResponse({"status":14404,"msg":"异常请求method,被拦截"})

        # request user agent
        self.user_agent = request.META["HTTP_USER_AGENT"]
        self.platform, self.browser = get_user_agent(self.user_agent)

        # request PATH
        self.path = request.path

        # request IP
        try:
            if "HTTP_X_FORWARDED_FOR" in request.META:
                self.ip = request.META["HTTP_X_FORWARDED_FOR"]
            else:
                self.ip = request.META["REMOTE_ADDR"]
        except Exception as e:
            return JsonResponse({"status":14404,"msg":"异常请求."})
        print(self.ip,self.user_agent,self.platform,self.browser)
            

    def process_view(self,request, view, args, kwargs):

        """
            1. check user identify
            2. check interface permission
            3. check product permission
        """
        # get token
        if request.path == "/api/user/login":
            return None
            
        token = ""
        if request.META.get("HTTP_AUTHORIZATION"):
            token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
        elif request.META.get("HTTP_AUTHENTICATION"):
            token = request.META["HTTP_AUTHENTICATION"].split(" ")[1]
        elif "token" in request.COOKIES:
            token = request.COOKIES["token"]
        else:
            return JsonResponse({"status":14402,"msg":"出错了,未取到token或cookie,请重新登录"})

        if token:
            pass
        else:
            return JsonResponse({"status":14402,"msg":"出错了，未取到token或cookie"})

        # check user token 
        try:
            user_data = Authentication.objects.\
                filter(token=token).\
                annotate(
                    identity=F("uid__identity"),
                    realname=F("uid__realname"),
                    user_status=F("uid__user_status")).\
                values("uid","identity","token","realname","user_status")[:][0]

            print("---------------------userinfo----------------")
            print(user_data,"\n")

        except Exception as e:
            print(e)
            return JsonResponse({"status": 14402, "msg": "身份令牌无效，请求中止"})
        else:
            if user_data["user_status"] == 2:
                return JsonResponse({"status": 14402, "msg": "已被封禁,请联系管理员."})

        # record log
        try:
            today = time.strftime("%Y-%m-%d", time.localtime())
            if "product_release" in self.path:
                flag = "登录"
                today_is_login = UserLog.objects.\
                    filter(
                        Q(create_time__gte=today) & 
                        Q(flag="登录") & 
                        Q(ip=self.ip)).\
                    values("id","user_id")
                if len(today_is_login) == 0:
                    record_log = UserLog(
                        user_id = get_user_object(request),
                        ip = self.ip,
                        flag = flag
                        )
                    record_log.save()
                else:
                    log_id = list(today_is_login)[0]['id']
                    record_log = UserLog.objects.get(id=log_id)
                    record_log.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    record_log.save()
        except Exception as e:
            print(e)
            pass

        # super path
        super_path = [
            "/api/system"
        ]

        # command path
        common_path = [
            "/api/support",
            "/api/user",
            "/api/qa/get_config",
            "/api/qa/create_config",
            "/api/pm/product"
        ]

        # required include product_id api_url
        required_include_product_path = [
            "/api/dashboard",
            "/api/analyze",
            "/api/pm/release",
            "/api/pm/member",
            "/api/pm/module",
            "/api/qa/bug/list",
            "/api/qa/bug/search",
            "/api/qa/bug/create",
            "/api/qa/bug/export",
            "/api/qa/bug/report",
            "/api/qa/testcase/list",
            "/api/qa/testcase/search",
            "/api/qa/testcase/export",
            "/api/qa/testcase/add",
            "/api/qa/testsuite/create",
            # "/api/qa/testsuite/list",
            "/api/qa/bug/report"
        ]

        print("--------------")
        print(user_data["identity"])

        # super/admin user
        if user_data["identity"] == 0:
            return None 

        # The average user
        if user_data["identity"] != "0" and self.path in super_path:
            return JsonResponse({"status":14444,"msg":"您的请求，超出了权限"})

        if self.path in common_path:
            return None
        else:
            if self.path in required_include_product_path:
                if not self.product_id:
                    return JsonResponse({"status":40004,"msg":"项目ID不能为空"})
                else:
                    user_id = user_data["uid"]

                    # 项目权限检查
                    query_product_role = ProductMembers.objects.\
                        filter(
                            Q(product_id=self.product_id) & 
                            Q(member_id=user_id) & 
                            Q(status=0)
                        ).\
                        values("role")[0]
                    if len(query_product_role) == 0:
                        return JsonResponse({"status":14444,"msg":"您不在此项目中,请联系管理员"})
                    else:
                        product_role = query_product_role["role"]

                        # 检查接口权限
                        print(product_role,self.path)
                        is_num = ApiPermissions.objects.\
                            filter(
                                Q(group=product_role) & 
                                Q(api_id__url=self.path) & 
                                Q(is_allow=1)).count()
                        if is_num == 1:
                            return None
                        else:
                            return JsonResponse({"status":14444,"msg":"您没有此接口的访问权限，请联系管理员"})

            
