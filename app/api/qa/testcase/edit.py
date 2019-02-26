#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product

from app.models import ModuleA
from app.models import ModuleB

from app.models import TestCase
from app.models import TestCaseFiles

from app.api.utils import get_listing
from app.api.auth import get_user_object

visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())

"""
    增加测试用例
"""
@csrf_exempt
@require_http_methods(["POST"])
def add(request):

    try:
        req = json.loads(request.body)
        product_id = req["product_id"]
        category = req["category"]
        title = req["title"]
        ExpectedResult = req["ExpectedResult"]
        steps = req["steps"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"产品信息、不能为空哦"})

    m1_obj,m2_obj = None,None
    if "module_id" in req and len(req["module_id"]):
        try:
            m1_obj = ModuleA.objects.get(m1_id=req["module_id"][0])
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
        try:
            if len(req["module_id"]) == 2:
                m2_id = req["module_id"][1]
                m2_obj = ModuleB.objects.get(m2_id=m2_id)
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})

    DataInput = ""
    precondition = ""
    remark = ""
    priority = ""
    if "DataInput" in req:
        DataInput = req["DataInput"]
    if "precondition" in req:
        precondition = req["precondition"]
    if "remark" in req:
        remark = req["remark"]
    if "priority" in req:
        priority = req["priority"]

    if len(title) > 50:
        return JsonResponse({"status":20004,"msg":"标题字数应小于50."})
    if len(DataInput) > 500:
        return JsonResponse({"status":20004,"msg":"输入字数应小于500."})
    if len(ExpectedResult) > 500:
        return JsonResponse({"status":20004,"msg":"预期结果字数应小于500."})
    if len(steps) > 5000:
        return JsonResponse({"status":20004,"msg":"操作步骤字数应小于5000."})
    if len(remark) > 1000:
        return JsonResponse({"status":20004,"msg":"备注字数应小于1000."})
    if len(precondition) > 200 or len(DataInput) > 200 or len(remark) > 1000:
        return JsonResponse({"status":20004,"msg":"超出字数限制。请检查前置条件、测试输入、备注项."})

    try:
        data = TestCase(
            product_id = Product.objects.get(product_id=product_id),
            title = title,
            category = category,
            DataInput = DataInput,
            steps = steps,
            expected_result = ExpectedResult,
            precondition = precondition,
            remark = remark,
            creator_id = get_user_object(request),
            priority = priority,
            m1_id = m1_obj,
            m2_id = m2_obj
            )
        data.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"用例保存失败"})
    else:
        case_id = TestCase.objects.get(case_id=data.case_id)
        # 保存附件
        try:
            if "annex" in req:
                if req["annex"]:
                    for f in req["annex"]:
                        file = TestCaseFiles(
                            case_id = case_id,
                            url = f
                            )
                        file.save()
        except Exception as e:
            TestCase.objects.get(case_id=case_id).delete()
            return JsonResponse({"status":20004,"msg":"附件错误"})
        else:
            return JsonResponse({"status":20000,"msg":"用例保存成功"})

"""
    修改测试用例
"""
@csrf_exempt
@require_http_methods(["POST"])
def edit(request):
    try:
        req = json.loads(request.body)
        testcase_id = req["case_id"]
        case_obj = TestCase.objects.get(case_id=testcase_id)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"用例ID不能为空,并且需有效"})

    if "DataInput" in req:
        case_obj.DataInput = req["DataInput"]
    if "precondition" in req:
        case_obj.precondition = req["precondition"]
    if "remark" in req:
        case_obj.remark = req["remark"]
    if "priority" in req:
        case_obj.priority = req["priority"]
    if "steps" in req:
        case_obj.steps = req["steps"]
    if "title" in req:
        case_obj.title = req["title"]
    if "expected_result" in req:
        case_obj.expected_result = req["expected_result"]
    if "category" in req:
        case_obj.category = req["category"]

    if "module_id" in req and req["module_id"]:
        try:
            m1_obj = ModuleA.objects.get(m1_id=req["module_id"][0])
            case_obj.m1_id = m1_obj
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
            
        if len(req["module_id"]) == 2:
            try:
                m2_obj = ModuleB.objects.get(m2_id=req["module_id"][1])
                case_obj.m2_id = m2_obj
            except Exception as e:
                return JsonResponse({"status": 40004, "msg": u"产品模块无效."})

    try:
        change_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        case_obj.isChange = 1
        case_obj.change_time = change_time
        case_obj.changer_id = get_user_object(request)
        case_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"修改失败"})
    else:
        # 保存附件
        try:
            if "annex" in req:
                annex = req["annex"]
                for f in annex:
                    aex = TestCaseFiles(
                        case_id = case_obj,
                        url = f
                        )
                    aex.save()
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"附件错误"})
        else:
            return JsonResponse({"status":20000,"msg":"修改成功"})
