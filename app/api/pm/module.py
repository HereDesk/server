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

"""
  模块
"""
@require_http_methods(["GET"])
def get_module(request):
    try:
        product_code = request.GET['product_code']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"product_code不能为空哦"})

    try:
        data = []
        module_a = ModuleA.objects.filter(product_code=product_code).\
            annotate(label=F('m1'),value=F('id')).\
            values('label','id','value').order_by('-id')
        for item in module_a:
            query = ModuleB.objects.filter(m1_id=item['id']).\
                annotate(label=F('m2'),value=F('id')).\
                values('label','id','value').order_by('-id')
            if len(query) > 0:
                item['children'] = list(query)
            data.append(item)
    except Exception as e:
        print(e)
        return JsonResponse({"status":40004,"msg":u"异常错误，请联系管理员."})
    else:
        return JsonResponse({"status":20000,"product_code":product_code,"data":data})

# 一级模块
@require_http_methods(["GET"])
def module_list_a(request):
    try:
        product_code = request.GET['product_code']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"product_code不能为空哦"})

    try:
        module = ModuleA.objects.filter(product_code=product_code).\
            values('product_code','m1','id').order_by('id')
    except Exception as e:
        return JsonResponse({"status":10004,"msg":u"异常错误，请联系管理员."})
    else:
        return JsonResponse({"status":20000,"product_code":product_code,"data":list(module)})

"""
  模块：增加
"""
@csrf_exempt
@require_http_methods(["POST"])
def module_add_a(request):

    try:
        rep = json.loads(request.body)
        product_code = rep['product_code']
        module_name = rep['ModuleA']
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"module是必填项哦"})
    else:
        if len(module_name) > 20:
            return JsonResponse({"status":20004,"msg":"名称长度的合理范围为2到20位"})

    n = ModuleA.objects.filter(Q(m1=module_name) & Q(product_code=product_code)).count()
    if n > 0:
        return JsonResponse({"status":20004,"msg":"名称已存在，请勿重复添加"})

    try:
        # 保存module
        pcode = Product.objects.get(product_code=product_code)
        m = ModuleA(
            product_code=pcode,
            m1=module_name,
            creator_id=get_user_object(request)
            )
        m.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"保存成功"})


# 二级模块
@require_http_methods(["GET"])
def module_list_b(request):
    try:
        module_a_id = request.GET['module_a_id']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"product_code不能为空哦"})

    try:
        module = ModuleB.objects.filter(Q(m1_id=module_a_id) & Q(isDelete=0)).\
            values('id','m2').order_by('id')
    except Exception as e:
        return JsonResponse({"status":10004,"msg":u"异常错误，请联系管理员."})
    else:
        return JsonResponse({"status":20000,"product_code":product_code,"data":list(module)})

"""
  二级模块：增加
"""
@csrf_exempt
@require_http_methods(["POST"])
def module_add_b(request):

    try:
        rep = json.loads(request.body)
        module_a_id = rep['module_a_id']
        module_b_name = rep['module_b_name']
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"module是必填项哦"})
    else:
        if len(module_b_name) > 20:
            return JsonResponse({"status":20004,"msg":"名称长度的合理范围为2到20位"})

    n = ModuleB.objects.filter(Q(m1_id=module_a_id) & Q(m2=module_b_name)).count()
    if n > 0:
        return JsonResponse({"status":20004,"msg":"此名称已存在，请勿重复添加"})

    try:
        # 保存module
        m = ModuleB(
            m1_id=ModuleA.objects.get(id=module_a_id),
            m2=module_b_name,
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
        m2_id = rep['id']
        m2_name = rep['m2']
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"缺少必填参数"})
    else:
        if len(m2_name) > 20:
            return JsonResponse({"status":20004,"msg":"名称长度的合理范围为2到20位"})

    try:
        m2_obj = ModuleB.objects.get(id=m2_id)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"该条记录不存在"})

    n = ModuleB.objects.filter(Q(id=m2_id) & Q(m2=m2_name)).count()
    if n > 0:
        return JsonResponse({"status":20004,"msg":"此名称已存在，请勿重复添加"})

    try:
        # 保存module
        m2_obj.m2=m2_name
        m2_obj.isChange = 1
        m2_obj.changer_id = get_user_object(request)
        m2_obj.change_time = curremt_time
        m2_obj.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"修改失败"})
    else:
        return JsonResponse({"status":20000,"msg":"修改成功"})


"""
  二级模块：删除
"""
@csrf_exempt
@require_http_methods(["GET"])
def module_del_b(request):

    try:
        m2_id = request.GET['id']
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"缺少必填参数"})

    try:
        m2_obj = ModuleB.objects.get(id=m2_id)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"该条记录不存在"})
    try:
        # 保存module
        m2_obj.isDelete = 1
        m2_obj.deleter_id = get_user_object(request)
        m2_obj.delete_time = curremt_time
        m2_obj.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"删除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"删除成功"})