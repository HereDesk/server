#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import time
import string
import xlsxwriter
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

from app.api.auth import get_user_object

visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())


"""
  case export
"""
@require_http_methods(["GET"])
def export(request):

    q1 = Q()
    q1.connector = "AND"

    try:
        req = request.GET.dict()
        product_id = req["product_id"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"产品名称不能为空"})
    else:
        q1.children.append(Q(**{"product_id":product_id}))

    if "m1_id" in req:
        m1_id = req["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))
    if "m2_id" in req:
        m1_id = req["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    test_data = TestCase.objects.filter(q1). \
        annotate(
            product_code=F("product_id__product_code"),
            creator=F("creator_id__realname"),
            changer=F("changer_id__realname"),
            m1_name=F("m1_id__m1_name"),
            m2_name=F("m2_id__m2_name")
            ).\
        values_list("id","product_code","m1_name","m2_name","precondition",
            "title","steps","expected_result","DataInput","remark",
            "priority","status",
            "creator","changer","create_time","change_time","last_time")[:]

    if len(test_data) == 0:
        return JsonResponse({"status":20004,"msg":"没有查到相关数据,请修改查询条件"})

    # 整理列数据
    table_data = []
    field_length = len(test_data[0])
    for n in range(0,field_length):
        temp = []
        for item in test_data:
            temp.append(item[n])
        table_data.append(temp)
    
    try:
        filename = 'Case_{0}.xlsx'.format(visualtime)
        filepath = 'media/export/' + filename
        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet('TestCase')

        # 工作表头部
        header_name = ['id','产品','一级模块','二级模块','前置条件','用例标题','步骤','预期结果',
            '测试数据','备注','优先级','状态','创建者','修改人','创建时间','修改时间','最后更新时间']
        cell_head = 'A1:{0}1'.format(string.ascii_uppercase[field_length])

        cell_head_format = workbook.add_format({
            "bold": True,
            "font_size": 13,
            "fg_color": "#EEEEEE",
            "locked":"True",
            'align':'vcenter'
            })
        worksheet.write_row(cell_head,header_name,cell_head_format)

        # 单元格高度
        cell_format = workbook.add_format({
            'align':'vcenter'
        })
        for row in range(0,len(test_data)+1):
            worksheet.set_row(row, 28)

        # 单元格宽度
        worksheet.set_column('F:F',50)
        worksheet.set_column('G:G',50)
        worksheet.set_column('H:H',50)
        worksheet.set_column('J:J',50)

        # 按列写入
        columns = [ chr(i) + '2' for i in range(65,65 + int(field_length))]

        for i,element in enumerate(columns):
            # 日期时间单元格格式
            if element in ['Q2','R2','T2']:
                cell_date_format = workbook.add_format({
                    'num_format':'yyyy/mm/dd hh:mm',
                    'align':'vcenter'
                })
                worksheet.write_column(element,table_data[i],cell_date_format)
            else:
                worksheet.write_column(element,table_data[i],cell_format)
    except Exception as e:
        print(e)
        return JsonResponse({"status":40001,"msg":"导出Excel时，写入文件失败"})
    else:
        workbook.close()
        return JsonResponse({"status":20000,"filename":filename,"url":"/"+filepath})