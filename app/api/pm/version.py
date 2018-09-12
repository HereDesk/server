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
        product_code = request.GET['product_code']
    except Exception as e:
        return JsonResponse({"status":40004,"msg":u"产品编号不能为空."})

    try:
        product = Product.objects.get(product_code=product_code)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":u"产品编号无效."})

    try:
        version_data = Release.objects.filter(product_code=product_code).\
            annotate(user=F('creator_id__realname')).\
            order_by('-create_time').values('product_code','version','create_time','user')
    except Exception as e:
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
        product_code = rep['product_code']
        release = rep['release']
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"产品名称和版本号是必填项哦"})

    # 检查产品是否存在
    try:
        pcode = Product.objects.get(product_code=product_code)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"未找到此产品名称"})

    # 检测版本号是否存在
    try:
        v = Release.objects.filter(Q(product_code=product_code) & Q(version=release)).count()
        if v > 0:
            return JsonResponse({"status":20004,"msg":"该版本号已存在"})
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"未找到此产品名称"})

    if len(release) > 20 | len(release) < 2:
        return JsonResponse({"status":20004,"msg":"名称长度的合理范围为2到20位"})

    try:
        p = Release(
            product_code = pcode,
            version = release,
            creator_id = get_user_object(request)
            )
        p.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"保存成功"})
