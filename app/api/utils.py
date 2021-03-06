#!/usr/bin/env python
# wandali

"""
  数据分页
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_listing(req_data,data):
    
    try:
        pageSize = req_data['pageSize']
        pageNumber = req_data['pageNumber']
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"缺少pageSize和pageNumber"})

    try:
        pageSize = int(pageSize)
        pageNumber = int(pageNumber)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"pageSize和pageNumber必须为整数"})
    else:
        if pageSize > 50:
            return JsonResponse({"status":20004,"msg":"做多一次只能请求50条数据哦"})
    try:
        paginator = Paginator(data, pageSize)
        contacts = paginator.page(pageNumber)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        return JsonResponse({"status":20001,"msg":u"别拉新了,我是有底线的"})
    else:
        return JsonResponse({"status":20000,"total":paginator.count,"data":list(contacts)})