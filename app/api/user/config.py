#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import json
from django.http import QueryDict
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import User

from app.models import SystemConfig
from app.models import UserConfig

from app.api.auth import get_user_object
from app.api.auth import get_uid

def set_cfg(request,code,code_value):
    uid = get_uid(request)
    data = UserConfig.objects.filter(Q(user_id=uid) & Q(code=code)).values_list("id","code_value")
    if data:
        cfg_id = data[0][0]
        try:
            cfg = UserConfig.objects.get(id=cfg_id)
            cfg.code_value = code_value
            cfg.save()
        except Exception as e:
            return JsonResponse({"status":20004})
    else:
        cfg = UserConfig(
            user_id = get_user_object(request),
            code = code,
            code_value = code_value
            )
        cfg.save()

"""
  用户信息
"""
@csrf_exempt
@require_http_methods(["GET"])
def user(request):

    req = request.GET
    if len(req) == 0:
        return JsonResponse({"status":40001,"msg":"请求参数不能为空!"})

    if "CASE_DATA_SHOW_STYPE" in req:
        code_value = req["CASE_DATA_SHOW_STYPE"]
        set_cfg(request,"CASE_DATA_SHOW_STYPE",code_value)
    if "BUG_DATA_SHOW_STYPE" in req:
        code_value = req["BUG_DATA_SHOW_STYPE"]
        set_cfg(request,"BUG_DATA_SHOW_STYPE",code_value)
    if "IS_SHOW_MODULE" in req:
        code_value = req["IS_SHOW_MODULE"]
        set_cfg(request,"IS_SHOW_MODULE",code_value)
        
    return JsonResponse({"status":20000})