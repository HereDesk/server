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

from app.models import TestCase
from app.models import TestCaseFiles

from app.api.utils import get_listing
from app.api.auth import get_user_object

visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())

"""
  测试用例：删除
"""
@csrf_exempt
@require_http_methods(["GET"])
def delete(request):
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
  Testcase: 附件删除
"""
@csrf_exempt
@require_http_methods(["POST"])
def annex_delete(request):
    try:
        req = json.loads(request.body)
        file_path = req["file_path"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"文件路径不能为空哦"})
    
    try:
        file_obj = TestCaseFiles.objects.get(file_path=file_path)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"没找到数据"})
    try:
        file_obj.isDelete = 1
        file_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"附件删除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"附件删除成功"})
