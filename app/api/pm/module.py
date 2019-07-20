#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release
from app.models import ModuleA
from app.models import ModuleB
from app.models import Authentication

from app.api.auth import get_user_object

# get cureent time
curremt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 所有模块
@require_http_methods(["GET"])
def module_list_all(request):
    try:
        product_id = request.GET["product_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"product_id不能为空哦"})

    product_data = Product.objects.filter(product_id=product_id).values_list("product_code",flat=True)

    try:
        data = []
        module_a = ModuleA.objects.filter(Q(product_id=product_id) & Q(is_delete=0)).\
            annotate(label=F("m1_name"),value=F("m1_id")).\
            values("label","m1_id","value").order_by("-id")
        for item in module_a:
            query = ModuleB.objects.filter(Q(m1_id=item["m1_id"]) & Q(is_delete=0)).\
                annotate(label=F("m2_name"),value=F("m2_id")).\
                values("label","m2_id","value").order_by("-id")
            if len(query) > 0:
                item["children"] = list(query)
            data.append(item)
    except Exception as e:
        print(e)
        return JsonResponse({"status":40004,"msg":u"异常错误，请联系管理员."})
    else:
        return JsonResponse({"status":20000,"product_id":product_id,"product_code":product_data[0],"data":data})

"""
  模块：增加
"""
@csrf_exempt
@require_http_methods(["POST"])
def module_add_a(request):

    try:
        rep = json.loads(request.body)
        product_id = rep["product_id"]
        m1_name = rep["m1_name"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"product_id、module是必填项哦"})
    else:
        if len(m1_name) > 20:
            return JsonResponse({"status":20004,"msg":"名称长度的合理范围为2到20位"})

    n = ModuleA.objects.filter(Q(m1_name=m1_name) & Q(product_id=product_id)).count()
    if n > 0:
        return JsonResponse({"status":20004,"msg":"名称已存在，请勿重复添加"})

    try:
        # 保存module
        product_obj = Product.objects.get(product_id=product_id)
        m = ModuleA(
            product_id=product_obj,
            m1_name=m1_name,
            creator_id=get_user_object(request)
            )
        m.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"一级模块保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"一级模块保存成功"})


"""
  二级模块：增加
"""
@csrf_exempt
@require_http_methods(["POST"])
def module_add_b(request):

    try:
        rep = json.loads(request.body)
        m1_id = rep["m1_id"]
        m2_name = rep["m2_name"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"module信息是必填项哦"})

    if len(m2_name) > 20:
        return JsonResponse({"status":20004,"msg":"名称长度的合理范围为2到20位"})

    n = ModuleB.objects.filter(Q(m1_id=m1_id) & Q(m2_name=m2_name)).count()
    if n > 0:
        return JsonResponse({"status":20004,"msg":"此名称已存在，请勿重复添加"})

    try:
        # 保存module
        m = ModuleB(
            m1_id=ModuleA.objects.get(m1_id=m1_id),
            m2_name=m2_name,
            creator_id=get_user_object(request)
            )
        m.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"保存成功"})

"""
  二级模块：编辑
"""
@csrf_exempt
@require_http_methods(["POST"])
def module_edit_b(request):

    try:
        rep = json.loads(request.body)
        m2_id = rep["m2_id"]
        m2_name = rep["m2_name"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"缺少必填参数"})
    else:
        if len(m2_name) > 20:
            return JsonResponse({"status":20004,"msg":"名称长度的合理范围为2到20位"})

    try:
        m2_obj = ModuleB.objects.get(m2_id=m2_id)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"该条记录不存在"})

    query_data = ModuleB.objects.filter(Q(m2_id=m2_id) & Q(m2_name=m2_name)).values("m2_name")
    if len(query_data) > 0:
        if list(query_data)[0]["m2_name"] == m2_name:
            return JsonResponse({"status":20004,"msg":"新提交的模块名称与旧模块名称相同"})

    try:
        m2_obj.m2_name=m2_name
        m2_obj.is_change = 1
        m2_obj.changer_id = get_user_object(request)
        m2_obj.change_time = curremt_time
        m2_obj.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"二级模块修改失败"})
    else:
        return JsonResponse({"status":20000,"msg":"二级模块修改成功"})


"""
  二级模块：删除
"""
@csrf_exempt
@require_http_methods(["GET"])
def module_del_b(request):

    try:
        m2_id = request.GET["m2_id"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"缺少必填参数"})

    try:
        m2_obj = ModuleB.objects.get(m2_id=m2_id)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"该条记录不存在"})
    try:
        # 保存module
        m2_obj.is_delete = 1
        m2_obj.deleter_id = get_user_object(request)
        m2_obj.delete_time = curremt_time
        m2_obj.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"删除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"删除成功"})
