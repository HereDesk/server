#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
from datetime import datetime
from django.utils.timezone import now, timedelta
from django.db.models.functions import TruncDate
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count
from django.db.models import Sum
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Authentication
from app.models import User

from app.models import Product
from app.models import ProductMembers
from app.models import TestCase

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_uid
from app.api.auth import get_myinfo


# 我今天的
@require_http_methods(['GET'])
def my_today(request):

    # tody
    today = time.strftime("%Y-%m-%d", time.localtime())

    # get user group and user_id
    my_info = get_myinfo(request)
    group = my_info['group']
    uid = my_info['uid']
    my_object = User.objects.get(user_id=uid)

    try:
        create = TestCase.objects.filter(Q(create_time__gte=today) & Q(creator_id=uid)).\
            aggregate(create=Count('create_time'))
    except Exception as e:
        print(e)
        return JsonResponse({'status':40004,"msg":"服务器开小差了，请联系管理员"})
    else:
        return JsonResponse({"status":20000, "group":group,"data": create})