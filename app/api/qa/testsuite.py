#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
import uuid
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
from app.models import ProductMembers

from app.models import Authentication

from app.models import Bug
from app.models import TestCase
from app.models import TestSuite
from app.models import TestSuiteCell

from app.api.utils import get_listing
from app.api.auth import get_uid
from app.api.auth import get_user_object

# get cureent time
curremt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

"""
testcase stuie add
"""
@csrf_exempt
@require_http_methods(["POST"])
def testsuite_create(request):
	try:
		req = json.loads(request.body)
		product_id = req["product_id"]
		suite_name = req["suite_name"]
		product_obj = Product.objects.get(product_id=product_id)
	except Exception as e:
		return JsonResponse({"status":40001,"msg":"缺少必要的请求参数"})

	if len(suite_name) > 30:
		return JsonResponse({"status":20004,"msg":"名称的有效长度需小于30"})
	
	try:
		suite_obj = TestSuite(
			suite_name = suite_name,
			product_id = product_obj,
			creator_id = get_user_object(request)
		)
		suite_obj.save()
	except Exception as e:
		print(e)
		return JsonResponse({"status":20004,"msg":"保存失败，请联系管理员"})
	else:
		return JsonResponse({"status":20000,"msg":"创建成功"})

"""
    testcase stuie list
"""
@csrf_exempt
@require_http_methods(["GET"])
def testsuite_list(request):
	user_id = get_uid(request)
	query_data = ProductMembers.objects.\
		filter(Q(member_id=user_id) & Q(status=0)).\
		annotate(
			product_name=F('product_id__product_name'),\
			create_time=F('product_id__create_time')).\
		values_list('product_id').\
		order_by('-create_time')
	product_list = list(query_data)
	try:
		suite_data = TestSuite.objects.\
			annotate(product_code=F("product_id__product_code")).\
			filter(product_id__in=product_list).\
			values("id","product_id","product_code","suite_id","suite_name").\
			order_by("-create_time")
		tmp = []
		for i in suite_data:
			i["bug_num"] = Bug.objects.filter(Q(cell_id__suite_id=i["suite_id"])).count()
			i["total"] = TestSuiteCell.objects.filter(Q(suite_id=i["suite_id"])).count()
			i["executed"] = TestSuiteCell.objects.filter(Q(suite_id=i["suite_id"]) & ~Q(result="0")).count()
			i["not_execution"] = TestSuiteCell.objects.filter(Q(suite_id=i["suite_id"]) & Q(result="0")).count()
			i["success"] = TestSuiteCell.objects.filter(Q(suite_id=i["suite_id"]) & Q(result="1")).count()
			i["fail"] = TestSuiteCell.objects.filter(Q(suite_id=i["suite_id"]) & Q(result="-1")).count()
			tmp.append(i)
	except Exception as e:
		print(e)
		return JsonResponse({"status":40001,"msg":"服务器开小差了"})
	else:
		return HttpResponse(get_listing(request.GET,tmp))

"""
  test suite cell list
"""
@csrf_exempt
@require_http_methods(["GET"])
def cell_brief_list(request):
	try:
		suite_id = request.GET["suite_id"]
	except Exception as e:
		return JsonResponse({"status":40001,"msg":"suite_id不能为空"})

	try:
		data = TestSuiteCell.objects.filter(Q(suite_id=suite_id)).\
			annotate(
                title=F("case_id__title"),
                creator=F("creator_id__realname"),
			).\
			values("cell_id","title","case_id","create_time","creator_id","creator")
	except Exception as e:
		return JsonResponse({"status":20004,"msg":"查询出错，请联系管理员"})
	else:
		return HttpResponse(get_listing(request.GET,data))

"""
  test suite cell list
"""
@csrf_exempt
@require_http_methods(["GET"])
def testsutie_cell_list(request):
	try:
		suite_id = request.GET["suite_id"]
	except Exception as e:
		return JsonResponse({"status":40001,"msg":"suite_id不能为空"})

	try:
		data = []
		suite_data = TestSuiteCell.objects.filter(Q(suite_id=suite_id)).\
			annotate(
          		title=F("case_id__title"),
				runner=F("runner_id__realname")
			).\
			values("id","title","case_id","result","run_time","runner","cell_id")
		for i in suite_data:
			cid = i['cell_id']
			tmp = Bug.objects.filter(Q(cell_id=cid)).values('bug_id')
			i['bug_id'] = list(tmp)
			data.append(i)
	except Exception as e:
		print(e)
		return JsonResponse({"status":20004,"msg":"查询出错，请联系管理员"})
	else:
		return HttpResponse(get_listing(request.GET,data))

"""
  test suite cell add 
"""
@csrf_exempt
@require_http_methods(["POST"])
def testsutie_cell_add(request):
	try:
		req = json.loads(request.body)
		suite_id = req["suite_id"]
	except Exception as e:
		return JsonResponse({"status":40001,"msg":"suite_id不能为空"})
	
	if "case_data" in req and "m1" not in req:
		case_data = req["case_data"]
	if "case_data" in req and "m1" in req:
		return JsonResponse({"status":40001,"msg":"请检查请求数据"})

	if "m1" in req:
		m1 = req["m1"]
		if "m2" in req:
			m2 = req["m2"]
			case_data = TestCase.objects.filter(Q(m2_id=m2)).values_list("case_id")[:]
		else:
			case_data = TestCase.objects.filter(Q(m1_id=m1)).values_list("case_id")[:]
		if len(case_data) == 0:
			return JsonResponse({"status":20004,"msg":"该模块下没有测试用例数据"})
		case_data = [ str(i[0]) for i in case_data]

	if len(case_data) == 0:
		return JsonResponse({"status":20004,"msg":"没有选中用例哦"})

	get_exist_data = TestSuiteCell.objects.filter(Q(suite_id=suite_id)).values_list("case_id")

	if get_exist_data:
		get_exist_data = [ str(i[0]) for i in get_exist_data ]

	after_case_data = [case for case in case_data if case not in get_exist_data]

	if len(after_case_data) == 0:
		return JsonResponse({"status":20004,"msg":"已存在，请选择其它用例"})
		
	try:
		creator_obj = get_user_object(request)
		suite_obj = TestSuite.objects.get(suite_id=suite_id)
		try:
			data = [ TestSuiteCell(
				case_id = TestCase.objects.get(case_id=i),
				suite_id = suite_obj,
				creator_id = creator_obj)
				for i in after_case_data ]
		except Exception as e:
			return JsonResponse({"status":20004,"msg":"用例ID无效"})
		else:
			TestSuiteCell.objects.bulk_create(data)
	except Exception as e:
		return JsonResponse({"status":20004,"msg":"保存失败，请联系管理员"})
	else:
		return JsonResponse({"status":20000,"msg":"保存成功"})

"""
  test suite cell run
"""
@csrf_exempt
@require_http_methods(["POST"])
def testsutie_cell_run(request):
	try:
		req = json.loads(request.body)
		cell_id = req["cell_id"]
		result = req["result"]
	except Exception as e:
		return JsonResponse({"status":40001,"msg":"cell_id和result不能为空"})
	
	if result == 1 or result == -1:
		pass
	else:
		JsonResponse({"status":40001,"msg":"result无效"})

	try:
		cell_obj = TestSuiteCell.objects.get(cell_id=cell_id)
		cell_obj.result = result
		cell_obj.runner_id = get_user_object(request)
		cell_obj.run_time = curremt_time
		cell_obj.save()
	except Exception as e:
		return JsonResponse({"status":20004,"msg":"服务器开小差了"})
	else:
		return JsonResponse({"status":20000,"msg":"用例运行结果保存成功"})

	