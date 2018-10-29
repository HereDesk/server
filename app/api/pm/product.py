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
from app.models import ModuleA
from app.models import Authentication
from app.models import ProductMembers

from app.api.auth import get_user_object
from app.api.auth import get_uid
from app.api.auth import _auth
from app.api.auth import get_myinfo

"""
  获取项目与版本（用户）
"""
@require_http_methods(["GET"])
def product_release(request):
    
    user_id = get_uid(request)
    product = ProductMembers.objects.filter(Q(member_id=user_id) & Q(status=0)).\
        annotate(product_name=F('product_code__product_name'),create_time=F('product_code__create_time')).\
        values('product_code','product_name').order_by('-create_time')
    if len(product) == 0:
        return JsonResponse({"status":20004,"msg":"检测到您不在任何项目列表中，请联系管理员添加！"})
    else:
        data = []
        for i in product:
            data.append({
                'product_code':i['product_code'],
                'product_name':i['product_name'],
                'data':list(Release.objects.filter(product_code=i['product_code']).values('version').order_by('-create_time'))
                })
        return JsonResponse({"status":20000,"data":data})

"""
  获取项目与版本（用户）
"""
@require_http_methods(["GET"])
def new_product_release(request):
    user_id = get_uid(request)
    product = ProductMembers.objects.filter(Q(member_id=user_id) & Q(status=0)).\
        annotate(product_name=F('product_code__product_name')).\
        values('product_code','product_name')
    if len(product) == 0:
        return JsonResponse({"status":20004,"msg":"检测到您不在任何项目列表中，请联系管理员添加！"})
    else:
        data = []
        for i in product:
            data.append({
                'value':i['product_code'],
                'label':i['product_name'],
                'children':list(Release.objects.filter(product_code=i['product_code']).\
                    annotate(value=F('version'),label=F('version'))
                    .values('value','label'))
                })
        return JsonResponse({"status":20000,"data":data})

"""
  获取项目与版本（用户）
"""
@require_http_methods(["GET"])
def user_product_list(request):
    user_id = get_uid(request)
    data = ProductMembers.objects.filter(Q(member_id=user_id) & Q(status=0)).\
        annotate(product_name=F('product_code__product_name'),create_time=F('product_code__create_time')).\
        values('product_code','product_name').order_by('-create_time')
    if len(data) == 0:
        return JsonResponse({"status":20004,"msg":"检测到您不在任何项目列表中，请联系管理员添加！"})
    else:
        return JsonResponse({"status":20000,"data":list(data)})

"""
 产品: 仅仅供admin调用
"""
# @csrf_exempt
@require_http_methods(["GET"])
def all_product_list(request):
    userinfo = get_myinfo(request)
    if userinfo["identity"] == 0 and userinfo["group"] == "admin":
        try:
            data = Product.objects.filter(status=0).\
                annotate(creator=F('creator_id__realname')).\
                order_by('-create_time').\
                values('product_name','product_code','create_time','creator')
        except Exception as e:
            return JsonResponse({"status":40004,"msg":u"异常错误，请联系管理员."})
    else:
        try:
            uid = userinfo["uid"]
            myself_product = Product.objects.filter(creator_id=uid).\
                annotate(
                    creator=F('creator_id__realname')
                ).\
                values('product_name','product_code','create_time','creator')
            my_join_product = ProductMembers.objects.filter(Q(member_id=uid) & Q(status=0)).\
                annotate(
                    product_name=F('product_code__product_name'),\
                    create_time=F('product_code__create_time'),
                    creator=F('product_code__creator_id__realname')).\
                values('product_code','product_name','create_time','creator')
            data = list(myself_product) + list(my_join_product)
        except Exception as e:
            return JsonResponse({"status":40004,"msg":u"异常错误，请联系管理员."})
    return JsonResponse({"status":20000,"data":list(data)})

"""
  产品：create
"""
@csrf_exempt
@require_http_methods(["POST"])
def create_product(request):
    rep = json.loads(request.body)

    try:
        product_code = rep['product_code']
        product_name = rep['product_name']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"产品名称和编号是必填项哦"})

    if len(product_code) > 20 | len(product_code) < 2:
        return JsonResponse({"status":20004,"msg":"名称长度的合理范围为1到20位"})
    if len(product_name) > 20 | len(product_name) < 2:
        return JsonResponse({"status":20004,"msg":"编号长度的合理范围为1到20位"})

    try:
        p = Product(
            product_code = product_code,
            product_name = product_name,
            principal = get_user_object(request),
            creator_id = get_user_object(request)
            )
        p.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"产品增加成功！快去增加产品版本、成员信息吧"})