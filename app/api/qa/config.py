#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from datetime import datetime
from datetime import datetime,timedelta

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

from app.models import User

from app.models import QaConfig

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_user_name
from app.api.auth import get_uid

"""
  qa config
"""
@require_http_methods(["GET"])
def get_qa_config(request):

    config_data = QaConfig.objects.all().values("config_name","config_value")

    if not config_data:
        return JsonResponse({"status":20004,"msg":"没查到数据"})

    try:    
        data = { i['config_name']:json.loads(i["config_value"])["data"] for i in config_data }
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"未查到有效的数据,请检查数据库数据"})
    else:
        return JsonResponse({"status":20000,"data":data})

"""
  qa config
"""
@csrf_exempt
@require_http_methods(["POST"])
def create_qa_config(request):

    try:
        req = json.loads(request.body)
        config_name = req["config_name"]
        config_value = req["config_value"]
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"参数无效"})

    if len(config_name) > 30:
        return JsonResponse({"status":20004,"msg":"配置名称长度需小于30"})

    if not isinstance(config_value,dict):
        return JsonResponse({"status":20004,"msg":"config_value的值必须是dict类型"})
    if not config_value:
        return JsonResponse({"status":20004,"msg":"config_value不能为空"})

    is_exist = QaConfig.objects.filter(config_name=config_name)

    if is_exist:
        return JsonResponse({"status":20004,"msg":"配置名称已存在"})

    try:
        cfg = QaConfig(
            config_name = config_name,
            config_value = config_value 
            )
        cfg.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"保存成功"})
    