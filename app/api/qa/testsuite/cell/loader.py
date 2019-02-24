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
  test suite cell list
"""
@csrf_exempt
@require_http_methods(["GET"])
def loader_list(request):
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
