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

from app.models import TestCase
from app.models import TestCaseFiles
from app.models import TestCaseReview

from app.api.utils import get_listing
from app.api.auth import get_user_object

visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())

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
                product_code=F("product_id__product_code"),
                creator=F("creator_id__realname"),
                changer=F("changer_id__realname"),
                deleter=F("deleter_id__realname"),
                faller=F("faller_id__realname"),
                m1_name=F("m1_id__m1_name"),
                m2_name=F("m2_id__m2_name")
                ).\
            values("id","case_id","category","product_id","product_code","priority","status",
                "m1_id","m2_id","m1_name","m2_name",
                "title","precondition","DataInput","steps","expected_result","remark",
                "creator_id","changer_id","deleter_id","creator","changer","deleter","faller","faller_id",
                "create_time","change_time","last_time","delete_time","fall_time")

        review = TestCaseReview.objects.filter(Q(case_id=case_id)).\
            annotate(realname=F("user_id__realname")).values("remark","realname","create_time","result")

        annex = TestCaseFiles.objects.filter(Q(case_id=case_id) & Q(is_delete=0)).values("url")

        annex_tmp = []
        for ax in annex:
            try:
                ax["suffix"] = str(ax["url"]).split('.')[-1]
            except Exception as e:
                ax["suffix"] = "unknow"
            annex_tmp.append(ax)
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        return JsonResponse({
            "status": 20000, 
            "data": list(data)[0],
            "review":list(review),
            "annex":list(annex_tmp)
        })