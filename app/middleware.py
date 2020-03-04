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
from django.shortcuts import render
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

def get_current_time():
    return datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")


def get_user_agent(user_agent):
    """
    获取agent
    """

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
        elif request.META.get("HTTP_COOKIE"):
            http_cookie = request.META.get("HTTP_COOKIE")
            http_cookie = http_cookie.replace(' ','')
            cookies = dict([l.split("=", 1) for l in http_cookie.split(";")])
            if "token" in cookies:
                token = cookies["token"]
            else:
                return JsonResponse({"status":14402,"msg":"出错了,token无效,请重新登录"})
        elif "token" in request.COOKIES:
            token = request.COOKIES["token"]
        else:
            return JsonResponse({"status":14402,"msg":"出错了,服务器未取到token或cookie,请重新登录"})

        if token:
            print("\nin the request, token is: {0}".format(token))
        else:
            return JsonResponse({"status":14402,"msg":"出错了,token无效,请重新登录"})

        # check user token
        try:
            user_data = Authentication.objects.\
                filter(token=token).\
                annotate(
                    identity=F("uid__identity"),
                    realname=F("uid__realname"),
                    user_status=F("uid__user_status")).\
                values("uid","identity","realname","user_status")[:][0]

            print("\n{0}-------------------------------------".format(get_current_time()))
            print("UserInfo:  {0} \n".format(user_data))

        except Exception as e:
            print(e)
            return JsonResponse({"status": 14402, "msg": "身份令牌无效，被阻拦，请求中止"})
        else:
            if user_data["user_status"] == 2:
                return JsonResponse({"status": 14402, "msg": "此用户已被封禁,请联系管理员."})

        # record log
        try:
            today = time.strftime("%Y-%m-%d", time.localtime())
            if "userinfo" in self.path:
                today_is_login = UserLog.objects.\
                    filter(
                        Q(create_time__gte=today) &
                        Q(user_id=user_data["uid"]) &
                        Q(flag="登录") &
                        Q(ip=self.ip)).\
                    values("id","user_id")
                if len(today_is_login) == 0:
                    record_log = UserLog(
                        user_id = get_user_object(request),
                        ip = self.ip,
                        flag = "登录")
                    record_log.save()
                else:
                    log_id = list(today_is_login)[0]['id']
                    robj = UserLog.objects.get(id=log_id)
                    robj.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    robj.save()
        except Exception as e:
            print(e)
            pass

        # super path
        super_path = "/api/system"

        # command path
        common_path = [
            "/api/support",
            "/api/user/info",
            "/api/qa/get_config",
            "/api/qa/create_config",
            "/api/pm/product"
        ]

        # required include product_id api_url
        required_include_product_path = [
            "/api/dashboard/data_statistics",
            "/api/analyze/bug/query",
            "/api/analyze/bug/date/create",
            "/api/user/pages",
            "/api/pm/module",
            "/api/pm/module/all/list",
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
            "/api/qa/testsuite/list",
            "/api/qa/bug/report"
        ]

        # super/admin user
        if user_data["identity"] == 0:
            return None

        # The average user
        if user_data["identity"] != "0" and super_path in self.path:
            return JsonResponse({"status":14444,"msg":"您的请求，超出了权限。只有超级管理员才能访问"})

        # 公共api
        if self.path in common_path:
            return None

        # 必须携带项目ID的api
        if self.path in required_include_product_path:
            if not self.product_id:
                return JsonResponse({"status":20004,"msg":"项目ID不能为空"})
            user_id = user_data["uid"]

            # 项目权限检查
            try:
                query_product_role = ProductMembers.objects.\
                    filter(
                        Q(product_id=self.product_id) &
                        Q(member_id=user_id) &
                        Q(status=0)
                    ).\
                    values("user_role")[0]
            except Exception as e:
                return JsonResponse({"status":20005,"msg":"项目ID无效"})

            if len(query_product_role) == 0:
                return JsonResponse({"status":14444,"msg":"您不在此项目中,请联系管理员"})
            else:
                product_role = query_product_role["user_role"]

                # 检查接口权限
                is_num = ApiPermissions.objects.\
                    filter(
                        Q(user_role=product_role) &
                        Q(api_id__url=self.path) &
                        Q(is_allow=1)).count()
                if is_num == 1:
                    return None
                else:
                    return JsonResponse({"status":14444,"msg":"您没有此接口的访问权限，请联系管理员"})
