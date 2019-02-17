#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
from datetime import datetime,timedelta
# from django.utils.timezone import now, timedelta
from django.db.models.functions import TruncDate
from django.db.models.functions import TruncHour
from django.db.models.functions import TruncMonth
from django.db.models.functions.datetime import ExtractMonth
from django.db.models.functions.datetime import ExtractHour
from django.db.models.functions.datetime import ExtractWeekDay
from django.db.models import Count, TimeField
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
from app.models import Release
from app.models import ProductMembers
from app.models import TestCase
from app.models import Bug

from app.api.utils import get_listing
from app.api.auth import get_user_object
from app.api.auth import get_uid
from app.api.auth import get_myinfo

# 查询统计
@require_http_methods(['GET'])
def query(request):
    q = Q()
    try:
        product_id = request.GET['product_id']
        q.children.append(Q(**{'product_id':product_id}))
        qtype = request.GET['type']
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": "请求缺少必要的值."})
    
    if 'version' in request.GET:
        version = request.GET['version']
        try:
            Release.objects.get(Q(version=version) & Q(product_id=product_id))
        except Exception as e:
            print(e)
            return JsonResponse({"status": 40001, "msg": "版本号无效"})
        else:
            q.children.append(Q(**{'version_id__version':version}))

    try:
        if qtype == 'status':
            data = Bug.objects.filter(q).annotate(name = F('status__name')).\
                values('name').annotate(value=Count('id'))
        elif qtype == 'severity':
            data = Bug.objects.filter(q).annotate(name = F('severity__name')).\
                values('name').annotate(value=Count('id'))
        elif qtype == 'priority':
            data = Bug.objects.filter(q).annotate(name = F('priority__name')).\
                values('name').annotate(value=Count('id'))
        elif qtype == 'bug_type':
            data = Bug.objects.filter(q).annotate(name = F('bug_type__name')).\
                values('name').annotate(value=Count('id'))
        else:
            data = []
    except Exception as e:
        return JsonResponse({'status':40004,"msg":"服务器开小差了，请联系管理员"})
    else:
        return JsonResponse({"status": 20000, "product_id": product_id,"data": list(data)})


# 按日期：新建bug
@require_http_methods(['GET'])
def date_create(request):

    q = Q()
    q.connector = 'AND'
    query_type_list = ['today','week','month','year','section']

    try:
        product_id = request.GET['product_id']
        qtype = request.GET['type']
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"产品与类型不能为空."})
    else:
        q.children.append(Q(**{'product_id':product_id}))
        if qtype not in query_type_list:
            return JsonResponse({"status":40001, "msg": "查询类型无效"})

    if qtype == 'section':
        try:
            start_date = request.GET['start_date']
            end_date = request.GET['end_date'] 
            end_date = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days = 1)
            q.children.append(Q(**{'create_time__gte':start_date}))
            q.children.append(Q(**{'create_time__lte':end_date}))
        except Exception as e:
            print(e)
            return JsonResponse({"status":40001, "msg": "开始日期和结束日期不能为空"})

    if qtype == 'month':
        month = time.strftime("%m", time.localtime())
        q.children.append(Q(**{'create_time__month':month}))

    if qtype == 'year':
        year = time.strftime("%Y", time.localtime())
        q.children.append(Q(**{"create_time__year":year}))

    if qtype == 'week':
        week = datetime.now().isocalendar()[1]
        q.children.append(Q(**{"create_time__week":week}))

    if qtype == 'today':
        td = time.strftime("%d", time.localtime())
        q.children.append(Q(**{"create_time__day":td}))

    try:
        data = []
        if qtype == 'section' or qtype == 'month':
            data = Bug.objects.filter(q).\
                annotate(datetime=TruncDate('create_time')).values('datetime').\
                annotate(num=Count('id'))
            # print(Bug.objects.filter(q).annotate(datetime=TruncDate('create_time')).
            # values('datetime').annotate(num=Count('id')).query)
        if qtype == 'year':
            data = Bug.objects.filter(q).\
                annotate(datetime=ExtractMonth('create_time')).values('datetime').\
                annotate(num=Count('id'))
        if qtype == 'today':
            data = Bug.objects.filter(q).\
                annotate(datetime=ExtractHour('create_time')).values('datetime').\
                annotate(num=Count('id'))
        if qtype == 'week':
            data = Bug.objects.filter(q).\
                annotate(datetime=ExtractWeekDay('create_time')).values('datetime').\
                annotate(num=Count('id'))

    except Exception as e:
        print(e)
        return JsonResponse({'status':40004,"msg":"服务器开小差了，请联系管理员"})
    else:
        return JsonResponse({"status": 20000, "product_id": product_id, "type":qtype, "data": list(data)})

# 我今天的
@require_http_methods(['GET'])
def my_today(request):

    # tody
    today = time.strftime("%Y-%m-%d", time.localtime())

    try:
        pcode = request.GET['product_id']
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": u"产品不能为空."})

    # get user group and user_id
    my_info = get_myinfo(request)
    # group = my_info['group']
    group = "tester"
    uid = my_info['uid']
    my_object = User.objects.get(user_id=uid)

    try:
        data = ''
        if group == 'developer' or group == 'test':
            fixed = Bug.objects.filter(
                    Q(fixed_time__gte=today) & 
                    Q(fixed_id=uid) & 
                    Q(product_id=pcode)
                ).\
                aggregate(fixed=Count('fixed_time'))
            residue = Bug.objects.filter(
                Q(assignedTo_id=uid) &
                ~Q(status='Fixed') &
                ~Q(status='Closed') &
                Q(product_id=pcode)).\
                aggregate(residue=Count('id'))
            create = Bug.objects.filter(
                    Q(create_time__gte=today) & 
                    Q(product_id=pcode)
                ).\
                aggregate(create=Count('create_time'))
            closed = Bug.objects.filter(
                    Q(closed_time__gte=today) &
                    Q(closed_id=uid) &
                    Q(status='Closed') &
                    Q(product_id=pcode)).\
                aggregate(closed=Count('closed_time'))
            data = dict(create,**closed,**fixed,**residue)
        else:
            fixed = Bug.objects.filter(
                    Q(fixed_time__gte=today) & 
                    Q(product_id=pcode)
                ).\
                aggregate(fixed=Count('fixed_time'))
            residue = Bug.objects.filter(
                    ~Q(status='Fixed') &
                    ~Q(status='Closed') &
                    Q(product_id=pcode)
                ).\
                aggregate(residue=Count('id'))
            create = Bug.objects.filter(
                    Q(create_time__gte=today) & 
                    Q(product_id=pcode)
                ).\
                aggregate(create=Count('create_time'))
            closed = Bug.objects.filter(
                    Q(closed_time__gte=today) & 
                    Q(status='Closed') & 
                    Q(product_id=pcode)).\
                aggregate(closed=Count('closed_time'))
            hangUp = Bug.objects.filter(
                    Q(hangUp_time__gte=today) & 
                    Q(status='Hang-Up') & 
                    Q(product_id=pcode)
                ).\
                aggregate(hangUp=Count('hangUp_time'))
            data = dict(create,**closed,**hangUp,**fixed,**residue)
    except Exception as e:
        print(e)
        return JsonResponse({'status':40004,"msg":"服务器开小差了，请联系管理员"})
    else:
        return JsonResponse({"status":20000, "group":group,"data": data})

# 按照测试人员统计
@require_http_methods(['GET'])
def tester(request):
    q = Q()
    try:
        product_id = request.GET['product_id']
        q.children.append(Q(**{'product_id':product_id}))
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": "请求缺少必要的值."})
    
    if 'version' in request.GET:
        version = request.GET['version']
        try:
            Release.objects.get(Q(version=version) & Q(product_id=product_id))
        except Exception as e:
            return JsonResponse({"status": 40001, "msg": "版本号无效"})
        else:
            q.children.append(Q(**{'version_id__version':version}))

    try:
        data = Bug.objects.filter(q).\
            annotate(name=F('creator_id__realname')).values('name').\
            annotate(value=Count('id'))
    except Exception as e:
        return JsonResponse({'status':40004,"msg":"服务器开小差了，请联系管理员"})
    else:
        return JsonResponse({"status":20000, "product_id":product_id,"data": list(data)})

# 按照开发人员统计
@csrf_exempt
@require_http_methods(['GET'])
def developer(request):
    q1 = Q()

    try:
        product_id = request.GET['product_id']
        q1.children.append(Q(**{'product_id':product_id}))
    except Exception as e:
        return JsonResponse({"status": 40001, "msg": "请求缺少必要的值."})
    
    if 'version' in request.GET:
        version = request.GET['version']
        try:
            Release.objects.get(Q(version=version) & Q(product_id=product_id))
        except Exception as e:
            return JsonResponse({"status": 40001, "msg": "版本号无效"})
        else:
            q1.children.append(Q(**{'version_id__version':version}))
    try:
        fixed_num = Bug.objects.filter(q1 & Q(status="Closed") | Q(status='Fixed')).\
            annotate(name=F('fixed_id__realname')).values('name').\
            annotate(fixed_num=Count('id'))
        not_fixed_num = Bug.objects.filter(q1 & ~Q(status="Closed") & ~Q(status='Fixed')).\
            annotate(name=F('assignedTo_id__realname')).values('name').\
            annotate(not_fixed_num=Count('id'))
        tmp = []
        d1 = list(fixed_num)
        d2 = list(not_fixed_num)
        for i1,v1 in enumerate(d1):
            for i2,v2 in enumerate(d2):
                if v1['name'] == v2['name']:
                    tmp.append(dict(v1,**v2))
                    del d1[d1.index(v1)]
                    del d2[d2.index(v2)]
        all_data = tmp + d1 + d2
        for i,v in enumerate(all_data):
            if all_data[i].get('fixed_num'):
                pass
            else:
                all_data[i]['fixed_num'] = 0
            if all_data[i].get('not_fixed_num'):
                pass
            else:
                all_data[i]['not_fixed_num'] = 0
    except Exception as e:
        print(e)
        return JsonResponse({'status':40004,"msg":"服务器开小差了，请联系管理员"})
    else:
        return JsonResponse({"status":20000, "product_id":product_id,"data": all_data})