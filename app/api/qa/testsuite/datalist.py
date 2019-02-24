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
    testcase stuie list
"""
@csrf_exempt
@require_http_methods(["GET"])
def data_list(request):
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