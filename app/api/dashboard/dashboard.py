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
from app.models import TestCase

from app.models import ProductMembers
from app.models import Authentication
from app.models import Bug

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_uid
from app.api.auth import get_user_group

@require_http_methods(['GET'])
def data_statistics(request):
    uid = get_uid(request)
    try:
        product_code = request.GET['product_code']
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"产品不能为空哦"})

    data = {
        "WaitPending": "",
        "Fixed":"",
        "NotFixed":"",
        "CreatedByMe":"",
        "ClosedByMe":"",
        "Resolved":""
    }
    # 分派给我(需要我处理的)
    try:
        my_group = get_user_group(request,product_id)
        if my_group == 'test':
            WaitPending = Bug.objects.\
                filter(
                    Q(assignedTo_id=uid) & 
                    Q(product_code=product_code) & 
                    ~Q(status='closed')
                ).count()
        else:
            WaitPending = Bug.objects.\
                filter(
                    Q(assignedTo_id=uid) & 
                    Q(product_code=product_code) & 
                    (
                        Q(status='Open') | 
                        Q(status='Hang-up') |
                        Q(status='Reopen')
                    )
                ).count()
    except Exception as e:
        WaitPending = 0
    finally:
        data['WaitPending']= WaitPending

    # 我解决的
    try:
        data_resolvedByMe = Bug.objects.filter(Q(product_code=product_code) & Q(fixed_id=uid)).count()
    except Exception as e:
        data_resolvedByMe = 0
    finally:
        data['ResolvedByMe']= data_resolvedByMe

    # 所有未解决的
    try:
        data_not_Fixed = Bug.objects.\
            filter(
                Q(product_code=product_code) & 
                ( 
                    Q(status='Open') | 
                    Q(status='Hang-up') |
                    Q(status='Reopen')
                )
            ).count()
    except Exception as e:
        data_not_Fixed = 0
    finally:
        data['NotFixed']= data_not_Fixed

    # 我创建的
    try:
        data_createdByMe = Bug.objects.filter(Q(product_code=product_code) & Q(creator_id=uid)).count()
    except Exception as e:
        data_createdByMe = 0
    finally:
        data['CreatedByMe']= data_createdByMe

    # 我关闭的
    try:
        data_closedByMe = Bug.objects.filter(Q(product_code=product_code) & Q(closed_id=uid)).count()
    except Exception as e:
        data_ClosedByMe = 0
    finally:
        data['ClosedByMe']= data_closedByMe

    # 所有已解决待关闭
    try:
        data_Fixed = Bug.objects.filter(Q(product_code=product_code) & Q(status='Fixed')).count()
    except Exception as e:
        data_Fixed = 0
    finally:
        data['Fixed']= data_Fixed

    return JsonResponse({"status":20000,"data":data})



