#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Group
from app.models import Product
from app.models import Release
from app.models import ModuleA
from app.models import Authentication
from app.models import ProductMembers

from app.api.auth import get_user_object
from app.api.auth import get_uid
from app.api.auth import _auth
from app.api.auth import get_myinfo
from app.api.auth import is_admin
"""
  获取项目与版本（用户）
"""
@require_http_methods(["GET"])
def product_release(request):
    
    user_id = get_uid(request)
    product = ProductMembers.objects.filter(Q(member_id=user_id) & Q(status=0)).\
        annotate(
            product_name=F('product_code__product_name'),
            create_time=F('product_code__create_time')).\
        values('product_code','product_name').order_by('-create_time')
    if len(product) == 0:
        return JsonResponse({"status":20004,"msg":"检测到您不在任何项目列表中，请联系管理员添加！"})
    else:
        data = []
        for i in product:
            data.append({
                'product_code':i['product_code'],
                'product_name':i['product_name'],
                'data':list(
                    Release.objects.filter(product_code=i['product_code']).\
                    values('version').order_by('-create_time')
                    )
                })
        return JsonResponse({"status":20000,"data":data})

"""
  cascader类型 获取项目与版本（用户）===仅仅用于统计
"""
@require_http_methods(["GET"])
def product_release_cascader(request):
    user_id = get_uid(request)
    product = ProductMembers.objects.\
        filter(Q(member_id=user_id) & Q(status=0)).\
        annotate(product_code=F('product_id__product_code')).\
        values('product_code','product_id')
    if len(product) == 0:
        return JsonResponse({"status":20004,"msg":"检测到您不在任何项目列表中，请联系管理员添加！"})
    else:
        data = []
        for i in product:
            data.append({
                'value':i['product_id'],
                'label':i['product_code'],
                'children':list(
                    Release.objects.filter(product_id=i['product_id']).\
                    annotate(value=F('version'),label=F('version')).\
                    values('value','label'))
                })
        return JsonResponse({"status":20000,"data":data})

"""
  获取当前自己的项目与版本（用户）
"""
@require_http_methods(["GET"])
def my_product_list(request):
    user_id = get_uid(request)
    is_admin_role = is_admin(request)
    print(is_admin_role)

    product = ProductMembers.objects.\
        filter(Q(member_id=user_id) & Q(status=0)).\
        annotate(
            product_name=F('product_id__product_name'),
            product_code=F('product_id__product_code'),
            create_time=F('product_id__create_time')
            ).\
        values('product_id','product_code','product_name').\
        order_by('-create_time')
    if len(product) == 0:
        if is_admin_role:
            return JsonResponse({"status":20004,"msg":"没有任何项目,赶快去创建吧"})
        else:
            return JsonResponse({"status":20004,"msg":"检测到您不在任何项目列表中，请联系管理员添加！"})
    else:
        data = []
        for i in product:
            data.append({
                'product_id':i['product_id'],
                'product_code':i['product_code'],
                'product_name':i['product_name'],
                'data':list(Release.objects.\
                    filter(product_id=i['product_id']).\
                    values('version').order_by('-create_time'))
                })
        return JsonResponse({"status":20000,"data":data})

"""
 产品: 仅仅供admin调用
"""
# @csrf_exempt
@require_http_methods(["GET"])
def all_product_list(request):
    userinfo = get_myinfo(request)
    if userinfo["identity"] == 0 and userinfo["username"] == "admin":
        try:
            admin_data = Product.objects.filter(status=0).\
                annotate(creator=F('creator_id__realname')).\
                order_by('-create_time').\
                values('product_id','product_name','product_code','create_time','creator','creator_id')
            data = list(admin_data)
            if data:
                for index,item in enumerate(data):
                    if item["creator_id"] == userinfo["uid"]:
                        data[index]["isCreator"] = True
                    else:
                        data[index]["isCreator"] = False
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":u"异常错误，请联系管理员."})
    else:
        try:
            uid = userinfo["uid"]
            user_data = ProductMembers.objects.\
                filter(Q(member_id=uid) & Q(status=0)).\
                annotate(
                    product_id=F('product_code__product_id'),\
                    product_name=F('product_code__product_name'),\
                    create_time=F('product_code__create_time'),
                    creator=F('product_code__creator_id__realname'),
                    creator_id=F('product_code__creator_id')).\
                values('product_id','product_code','product_name','create_time','creator','creator_id')
            data = list(user_data)
            if data:
                for index,item in enumerate(data):
                    if uid == item["creator_id"]:
                        data[index]["isCreator"] = True
                    else:
                        data[index]["isCreator"] = False

        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":u"异常错误，请联系管理员."})
    return JsonResponse({"status":20000,"identity":userinfo["identity"],"data":list(data)})

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

    if len(product_code) > 20 or len(product_code) < 3:
        return JsonResponse({"status":20004,"msg":"名称长度的合理范围为3到20位"})
    if len(product_name) > 20 or len(product_name) < 3:
        return JsonResponse({"status":20004,"msg":"编号长度的合理范围为3到20位"})

    is_check = Product.objects.\
        filter(Q(product_code=product_code) | Q(product_name=product_name)).\
        count()
    if is_check > 0:
        return JsonResponse({"status":"20004","msg":"此项目名称已存在哦"})
    try:
        prod = Product(
            product_code = product_code,
            product_name = product_name,
            principal = get_user_object(request),
            creator_id = get_user_object(request)
            )
        prod.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        try:
            member = ProductMembers(
                member_id = get_user_object(request),
                product_id = prod,
                role = Group.objects.get(group="originator"),
                status = 0
                )
            member.save()
        except Exception as e:
            print(e)
            pass
        return JsonResponse({"status":20000,"msg":"产品增加成功！快去增加产品版本、成员信息吧"})