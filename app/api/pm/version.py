#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release
from app.models import Authentication
from app.api.auth import get_user_object
from app.api.auth import _auth
"""
  版本
"""
@require_http_methods(["GET"])
def get_release(request):
    try:
        product_id = request.GET["product_id"]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":u"产品ID不能为空."})

    try:
        product_obj = Product.objects.get(product_id=product_id)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":u"产品ID无效."})

    try:
        version_data = Release.objects.\
            filter(product_id=product_id).\
            annotate(
                user=F("creator_id__realname"),
                product_code=F("product_id__product_code"),
                product_name=F("product_id__product_name")
                ).\
            order_by("-create_time").\
            values("product_id","product_name","product_code","version","create_time","user")
    except Exception as e:
        print(e)
        return JsonResponse({"status":40004,"msg":u"异常错误，请联系管理员."})
    else:
        return JsonResponse({"status":20000,"data":list(version_data)})
        

"""
  版本号：create
"""
@csrf_exempt
@require_http_methods(["POST"])
def create_release(request):
    rep = json.loads(request.body)

    try:
        product_id = rep["product_id"]
        release = rep["release"]
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"请求缺少产品ID和版本号名称"})

    # 检查产品是否存在
    try:
        product_obj = Product.objects.get(product_id=product_id)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"未找到此产品名称"})

    # 检测版本号是否存在
    try:
        v = Release.objects.filter(Q(product_id=product_id) & Q(version=release)).count()
        if v > 0:
            return JsonResponse({"status":20004,"msg":"该版本号已存在"})
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"未找到此产品名称"})

    if len(release) > 20 | len(release) < 3:
        return JsonResponse({"status":20004,"msg":"版本号的有效长度为3到20位"})

    try:
        p = Release(
            product_id = product_obj,
            version = release,
            creator_id = get_user_object(request)
            )
        p.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"保存成功"})
