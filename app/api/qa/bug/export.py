#!/usr/bin/env python
# -*- coding:utf8 -*-
import json
import time
import string
from datetime import datetime
import xlsxwriter

from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Count

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release

from app.models import Bug

# get cureent time
visualtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())

"""
  bug export
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
    print(req)
    if "release" in req:
        try:
            release = req["release"]
            if release == "all":
                del req["release"]
            else:
                release_query = Release.objects.\
                    filter(Q(product_id=product_id) & Q(version=release)).\
                    values('id')
                if len(release_query) == 0:
                    return JsonResponse({"status":40004,"msg":"版本号错误"})
                else:
                    q1.children.append(Q(**{"version_id":list(release_query)[0]['id']}))
        except Exception as e:
            print(e)
            return JsonResponse({"status":40004,"msg":"产品名称或版本号错误"})

    if "status" in req:
        if req["status"] == "all":
            del req["status"]
        elif req["status"] == "notClosed":
            q1.children.append(~Q(**{"status":"Closed"}))
        else:
            status = req["status"]
            q1.children.append(Q(**{"status":status}))

    bug_data = Bug.objects.filter(q1).\
        annotate(
                product_code=F("product_id__product_code"),
                creator_user=F("creator_id__realname"),
                assignedTo_user=F("assignedTo_id__realname"),
                fixed_user=F("fixed_id__realname"),
                closed_user=F("closed_id__realname"),
                severity_name=F("severity__name"),
                status_name = F("status__name"),
                solution_name=F("solution__name"),
                release=F("version_id__version"),
                bug_type_name=F("bug_type__name"),
                m1_name=F("m1_id__m1_name"),
                m2_name=F("m2_id__m2_name")
            ).\
        order_by("-id").\
        values_list("id","product_code","release","m1_name","title","status_name",
            "priority","severity_name","solution_name",\
            "creator_user","create_time","assignedTo_user","assignedTo_time",\
            "fixed_user","fixed_time","closed_user","closed_time","bug_type_name")[:]

    if len(bug_data) == 0:
        return JsonResponse({"status":20004,"msg":"没有查到相关数据,请修改查询条件"})

    # 准备行数据
    # table_data = bug_data
    # field_length = len(bug_data[0])

    # 整理列数据
    table_data = []
    field_length = len(bug_data[0])
    for n in range(0,field_length):
        temp = []
        for item in bug_data:
            temp.append(item[n])
        table_data.append(temp)
    
    try:
        filename = 'Bug_{0}.xlsx'.format(visualtime)
        filepath = 'media/export/' + filename
        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet('Bug')

        # 工作表头部
        header_name = ['id','产品','版本','模块','标题','状态','优先级','严重程度','缺陷类型',
            '解决方案','创建人','创建时间','指派给谁','指派时间','解决者','修复时间','关闭者','关闭时间']
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
        for row in range(0,len(bug_data)+1):
            worksheet.set_row(row, 28)

        # 单元格宽度
        worksheet.set_column('E:E',80)
        worksheet.set_column('K:K',15)
        worksheet.set_column('M:M',15)
        worksheet.set_column('O:O',15)
        worksheet.set_column('Q:Q',15)

        # 缺陷状态栏，按条件筛选
        caption = ('Cells with values == 1 are in light red. '
           'Values > 100 are in light green.')
        for n in range(2,len(bug_data)):
            print('A'+ str(n))
            worksheet.write('A'+ str(n), caption)

        # 按行写入
        # rows_num = len(table_data) + 1
        # rows = [ 'A' + str(i) for i in range(2,rows_num)]
        # for i,element in enumerate(rows):
        #     worksheet.write_row(element,table_data[i],cell_format)

        # 按列写入
        columns = [ chr(i) + '2' for i in range(65,65 + int(field_length))]

        for i,element in enumerate(columns):
            # 日期时间单元格格式
            if element in ['K2','M2','O2','Q2']:
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
