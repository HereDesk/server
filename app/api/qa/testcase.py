#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count
from django.db.models import Sum
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release

from app.models import ModuleA
from app.models import ModuleB
from app.models import Authentication

from app.models import TestCase
from app.models import TestCaseReview

from app.api.utils import get_listing
from app.api.auth import get_user_object

"""
  case详情
"""
@csrf_exempt
@require_http_methods(["GET"])
def details(request):

    try:
        case_id = request.GET["case_id"]
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": u"请求参数错误."})
        
    try:
        data = TestCase.objects. \
            filter(Q(case_id=case_id)). \
            annotate(
                creator=F("creator_id__realname"),
                changer=F("changer_id__realname"),
                deleter=F("deleter_id__realname"),
                faller=F("faller_id__realname"),
                m1_name=F("m1_id__m1"),
                m2_name=F("m2_id__m2")
                ).\
            values("id","case_id","category","product_code","priority","status","m1_id","m2_id","m1_name","m2_name",
                "title","precondition","DataInput","steps","expected_result","remark",
                "creator_id","changer_id","deleter_id","creator","changer","deleter","faller","faller_id",
                "create_time","change_time","update_time","delete_time","fall_time")

        review = TestCaseReview.objects.filter(Q(case_id=case_id)).\
            annotate(realname=F("user_id__realname")).values("remark","realname","create_time","result")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        return JsonResponse({"status": 20000, "data": list(data)[0],"review":list(review)})

"""
  搜索结果
"""
@csrf_exempt
@require_http_methods(["GET"])
def search(request):

    try:
        wd = request.GET["wd"]
        product_code = request.GET["product_code"]
    except Exception as e:
         return JsonResponse({"status": 40004, "msg": u"请求参数错误."})

    if "status" in request.GET:
        status = request.GET["status"]
    else:
        status = 0

    try:
        data = TestCase.objects.\
            filter(Q(product_code=product_code) &
                Q(status=status) &
                Q(isDelete=0) &
                Q(title__icontains=wd) |
                Q(id__icontains=wd)
                ).\
            annotate(
                creator=F("creator_id__realname")
                ).\
            values("id","case_id","product_code","status","title","priority",
                "isChange","isReview","creator","creator_id","create_time")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        if len(data) == 0:
            return JsonResponse({"status": 20001, "msg": "根据搜索条件，没有查到数据"})
        else:
            return HttpResponse(get_listing(request.GET,data))

"""
 测试用例LIST
"""
@csrf_exempt
@require_http_methods(["GET"])
def testcase_list(request):
    q1 = Q()
    q1.connector = "AND"

    try:
        product_code = request.GET["product_code"]
        q1.children.append(Q(**{"product_code":product_code}))
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求值"})

    if "m2_id" in request.GET:
        m2_id = request.GET["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    if "status" in request.GET:
        status = request.GET["status"]
        q1.children.append(Q(**{"status":status}))
            
    try:
        data = TestCase.objects.\
            filter(q1).\
            annotate(
                creator=F("creator_id__realname")
                ).\
            values("id","case_id","product_code","status","title","priority",
                "isChange","isReview","creator","creator_id","create_time")
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": u"查询发生异常错误，请联系管理员."})
    else:
        return HttpResponse(get_listing(request.GET,data))

"""
 测试用例LIST
"""
@csrf_exempt
@require_http_methods(["GET"])
def testcase_valid_list(request):
    q1 = Q()
    q1.connector = "AND"

    try:
        print()
        product_code = request.GET["product_code"]
        q1.children.append(Q(**{"product_code":product_code}))
    except Exception as e:
        print(e)
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求值"})

    if "m2_id" in request.GET:
        m2_id = request.GET["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    if "m1_id" in request.GET:
        m1_id = request.GET["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))
            
    try:
        q1.children.append(Q(**{"isDelete":0}))
        q1.children.append(Q(**{"status":0}))
        data = TestCase.objects.\
            filter(q1).\
            values("case_id","title").order_by("id")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        return HttpResponse(get_listing(request.GET,data))

"""
    增加测试用例
"""
@csrf_exempt
@require_http_methods(["POST"])
def add(request):
    res = json.loads(request.body)

    try:
        product_code = res["product_code"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"产品信息不能为空哦"})

    try:
        category = res["category"]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"用例类型不能为空哦"})

    if "module_id" in res and len(res["module_id"]):
        try:
            m1_id = ModuleA.objects.get(id=res["module_id"][0])
            m2_id = ModuleB.objects.get(id=res["module_id"][1])
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
    else:
        m1_id = None
        m2_id = None

    try:
        DataInput = ""
        precondition = ""
        remark = ""
        priority = ""
        title = res["title"]
        ExpectedResult = res["ExpectedResult"]
        steps = res["steps"]
        if "DataInput" in res:
            DataInput = res["DataInput"]
        if "precondition" in res:
            precondition = res["precondition"]
        if "remark" in res:
            remark = res["remark"]
        if "priority" in res:
            priority = res["priority"]
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"测试标题、步骤、预期结果不能为空哦"})

    if len(title) > 50:
        return JsonResponse({"status":20004,"msg":"标题字数应小于50."})
    if len(DataInput) > 500:
        return JsonResponse({"status":20004,"msg":"输入字数应小于500."})
    if len(ExpectedResult) > 500:
        return JsonResponse({"status":20004,"msg":"预期结果字数应小于500."})
    if len(steps) > 1000:
        return JsonResponse({"status":20004,"msg":"操作步骤字数应小于1000."})
    if len(remark) > 1000:
        return JsonResponse({"status":20004,"msg":"备注字数应小于1000."})
    if len(precondition) > 200 or len(DataInput) > 200 or len(remark) > 1000:
        return JsonResponse({"status":20004,"msg":"超出字数限制。请检查前置条件、测试输入、备注项."})

    try:
        d = TestCase(
                product_code = Product.objects.get(product_code=product_code),
                title = title,
                category = category,
                DataInput = DataInput,
                steps = steps,
                expected_result = ExpectedResult,
                precondition = precondition,
                remark = remark,
                creator_id = get_user_object(request),
                priority = priority,
                m1_id = m1_id,
                m2_id = m2_id
            )
        d.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"保存失败"})
    else:
        return JsonResponse({"status":20000,"msg":"保存成功"})

"""
  测试用例：失效操作
"""
@csrf_exempt
@require_http_methods(["GET"])
def fall(request):
    try:
        case_id = request.GET["case_id"]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"case_id不能为空"})

    try:
        case_id = TestCase.objects.get(case_id=case_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"case_id无效"})

    try:
        case_id.status = 1
        case_id.faller_id = get_user_object(request)
        case_id.fall_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        case_id.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"操作失败"})
    else:
        return JsonResponse({"status":20000,"msg":"操作成功"})

"""
  测试用例：删除
"""
@csrf_exempt
@require_http_methods(["GET"])
def del_testcase(request):
    try:
        rep = request.GET
        testcase_id = rep["case_id"]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"缺陷ID不能为空"})


    is_check_testcase = TestCase.objects.filter(case_id=testcase_id).values_list("isDelete")
    if len(is_check_testcase) == 0:
        return JsonResponse({"status":20004,"msg":"该条记录不存在"})
    try:
        if is_check_testcase[0][0] == 1:
            return JsonResponse({"status":20001,"msg":"该条记录已被他人删除"})
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"异常错误，请联系管理员"})
        
    try:
        tc = TestCase.objects.get(case_id=testcase_id)
        tc.deleter_id = get_user_object(request)
        tc.delete_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tc.isDelete = 1
        tc.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"删除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"删除成功"})


"""
    修改测试用例
"""
@csrf_exempt
@require_http_methods(["POST"])
def edit(request):
    try:
        res = json.loads(request.body)
        testcase_id = res["case_id"]
        ttc = TestCase.objects.get(case_id=testcase_id)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"用例ID不能为空,并且需有效"})

    if "DataInput" in res:
        ttc.DataInput = res["DataInput"]
    if "precondition" in res:
        ttc.precondition = res["precondition"]
    if "remark" in res:
        ttc.remark = res["remark"]
    if "priority" in res:
        ttc.priority = res["priority"]
    if "steps" in res:
        ttc.steps = res["steps"]
    if "title" in res:
        ttc.title = res["title"]
    if "expected_result" in res:
        ttc.expected_result = res["expected_result"]
    if "category" in res:
        ttc.category = res["category"]

    if "module_id" in res and len(res["module_id"]):
        try:
            m1_id = ModuleA.objects.get(id=res["module_id"][0])
            m2_id = ModuleB.objects.get(id=res["module_id"][1])
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
        else:
            ttc.m1_id = m1_id
            ttc.m2_id = m2_id
    try:
        change_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ttc.change_time = change_time
        ttc.changer_id = get_user_object(request)
        ttc.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"修改失败"})
    else:
        return JsonResponse({"status":20000,"msg":"修改成功"})

"""
  评审
"""
@csrf_exempt
@require_http_methods(["POST"])
def review(request):

    try:
        res = json.loads(request.body)
        case_id = res["case_id"]
        result = res["result"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"Result和case_id不能为空"})

    if result in [1,2]:
        pass
    else:
        return JsonResponse({"status":40001,"msg":"Result无效"})

    if "remark" in res:
        remark = res["remark"]
    else:
        remark = ""

    try:
        case_obj = TestCase.objects.get(case_id=case_id)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"case_id无效"})

    try:
        case_obj.isReview = result
        case_obj.save()

        review_result = TestCaseReview(
            user_id = get_user_object(request),
            case_id = case_obj,
            result = result,
            remark = remark
            )
        review_result.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"操作失败"})
    else:
        return JsonResponse({"status":20000,"msg":"操作成功"})