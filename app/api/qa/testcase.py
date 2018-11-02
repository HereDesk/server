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
from django.db.models import Count
from django.db.models import Sum
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Product
from app.models import Release

from app.models import ModuleA
from app.models import ModuleB
from app.models import Authentication

from app.models import TestCase
from app.models import TestCaseFiles
from app.models import TestCaseReview

from app.api.utils import get_listing
from app.api.auth import get_user_object

visualtime = time.strftime("%Y%m%d%H%M%S", time.localtime())

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
                creator=F("creator_id__realname"),
                changer=F("changer_id__realname"),
                deleter=F("deleter_id__realname"),
                faller=F("faller_id__realname"),
                m1_name=F("m1_id__m1"),
                m2_name=F("m2_id__m2")
                ).\
            values("id","case_id","category","product_code","priority","status","m1_id","m2_id","m1_name","m2_name",
                "title","precondition","DataInput","steps","expected_result","remark",
                "creator_id","changer_id","deleter_id","creator","changer","deleter","faller","faller_id",
                "create_time","change_time","update_time","delete_time","fall_time")

        review = TestCaseReview.objects.filter(Q(case_id=case_id)).\
            annotate(realname=F("user_id__realname")).values("remark","realname","create_time","result")

        annex = TestCaseFiles.objects.filter(Q(case_id=case_id) & Q(isDelete=0)).values("file_path")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        return JsonResponse({"status": 20000, "data": list(data)[0],"review":list(review),"annex":list(annex)})

"""
  搜索结果
"""
@csrf_exempt
@require_http_methods(["GET"])
def search(request):

    try:
        wd = request.GET["wd"]
        product_code = request.GET["product_code"]
    except Exception as e:
         return JsonResponse({"status": 40004, "msg": u"请求参数错误."})

    if "status" in request.GET:
        status = request.GET["status"]
    else:
        status = 0

    try:
        data = TestCase.objects.\
            filter(Q(product_code=product_code) &
                Q(status=status) &
                Q(isDelete=0) & (
                Q(title__icontains=wd) | 
                Q(id__icontains=wd))
                ).\
            annotate(
                creator=F("creator_id__realname")
                ).\
            values("id","case_id","product_code","status","title","priority",
                "isChange","isReview","creator","creator_id","create_time")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        if len(data) == 0:
            return JsonResponse({"status": 20001, "msg": "根据搜索条件，没有查到数据"})
        else:
            return HttpResponse(get_listing(request.GET,data))

"""
 测试用例LIST
"""
@csrf_exempt
@require_http_methods(["GET"])
def testcase_list(request):
    q1 = Q()
    q1.connector = "AND"

    try:
        product_code = request.GET["product_code"]
        q1.children.append(Q(**{"product_code":product_code}))
    except Exception as e:
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求值"})

    if "m1_id" in request.GET:
        m1_id = request.GET["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))

    if "m2_id" in request.GET:
        m2_id = request.GET["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    if "status" in request.GET:
        status = request.GET["status"]
        q1.children.append(Q(**{"status":status}))
            
    try:
        data = TestCase.objects.\
            filter(q1).\
            annotate(
                creator=F("creator_id__realname")
                ).\
            values("id","case_id","product_code","status","title","priority",
                "isChange","isReview","creator","creator_id","create_time").\
            order_by("-create_time")
    except Exception as e:
        return JsonResponse({"status": 20004, "msg": u"查询发生异常错误，请联系管理员."})
    else:
        return HttpResponse(get_listing(request.GET,data))

"""
 测试用例LIST
"""
@csrf_exempt
@require_http_methods(["GET"])
def testcase_valid_list(request):
    q1 = Q()
    q1.connector = "AND"

    try:
        print()
        product_code = request.GET["product_code"]
        q1.children.append(Q(**{"product_code":product_code}))
    except Exception as e:
        print(e)
        return JsonResponse({"status": 40004, "msg": "缺少必要的请求值"})

    if "m2_id" in request.GET:
        m2_id = request.GET["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    if "m1_id" in request.GET:
        m1_id = request.GET["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))
            
    try:
        q1.children.append(Q(**{"isDelete":0}))
        q1.children.append(Q(**{"status":0}))
        data = TestCase.objects.\
            filter(q1).\
            values("id","case_id","title").order_by("id")
    except Exception as e:
        print(e)
        return JsonResponse({"status": 20004, "msg": u"查询异常错误，请联系管理员."})
    else:
        return HttpResponse(get_listing(request.GET,data))

"""
    增加测试用例
"""
@csrf_exempt
@require_http_methods(["POST"])
def add(request):
    req = json.loads(request.body)

    try:
        product_code = req["product_code"]
        category = req["category"]
        title = req["title"]
        ExpectedResult = req["ExpectedResult"]
        steps = req["steps"]
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"产品信息、不能为空哦"})

    if "module_id" in req and len(req["module_id"]):
        try:
            m1_id = ModuleA.objects.get(id=req["module_id"][0])
            m2_id = ModuleB.objects.get(id=req["module_id"][1])
        except Exception as e:
            return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
    else:
        m1_id = None
        m2_id = None

    DataInput = ""
    precondition = ""
    remark = ""
    priority = ""
    if "DataInput" in req:
        DataInput = req["DataInput"]
    if "precondition" in req:
        precondition = req["precondition"]
    if "remark" in req:
        remark = req["remark"]
    if "priority" in req:
        priority = req["priority"]

    if len(title) > 50:
        return JsonResponse({"status":20004,"msg":"标题字数应小于50."})
    if len(DataInput) > 500:
        return JsonResponse({"status":20004,"msg":"输入字数应小于500."})
    if len(ExpectedResult) > 500:
        return JsonResponse({"status":20004,"msg":"预期结果字数应小于500."})
    if len(steps) > 5000:
        return JsonResponse({"status":20004,"msg":"操作步骤字数应小于5000."})
    if len(remark) > 1000:
        return JsonResponse({"status":20004,"msg":"备注字数应小于1000."})
    if len(precondition) > 200 or len(DataInput) > 200 or len(remark) > 1000:
        return JsonResponse({"status":20004,"msg":"超出字数限制。请检查前置条件、测试输入、备注项."})

    try:
        data = TestCase(
            product_code = Product.objects.get(product_code=product_code),
            title = title,
            category = category,
            DataInput = DataInput,
            steps = steps,
            expected_result = ExpectedResult,
            precondition = precondition,
            remark = remark,
            creator_id = get_user_object(request),
            priority = priority,
            m1_id = m1_id,
            m2_id = m2_id
            )
        data.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"用例保存失败"})
    else:
        case_id = TestCase.objects.get(case_id=data.case_id)
        # 保存附件
        try:
            if "annex" in req:
                if req["annex"]:
                    for f in req["annex"]:
                        file = TestCaseFiles(
                            case_id = case_id,
                            file_path = f
                            )
                        file.save()
        except Exception as e:
            TestCase.objects.get(case_id=case_id).delete()
            return JsonResponse({"status":20004,"msg":"附件错误"})
        else:
            return JsonResponse({"status":20000,"msg":"用例保存成功"})

"""
  测试用例：失效操作
"""
@csrf_exempt
@require_http_methods(["GET"])
def fall(request):
    try:
        case_id = request.GET["case_id"]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"case_id不能为空"})

    try:
        case_id = TestCase.objects.get(case_id=case_id)
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"case_id无效"})

    try:
        case_id.status = 1
        case_id.faller_id = get_user_object(request)
        case_id.fall_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        case_id.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"操作失败"})
    else:
        return JsonResponse({"status":20000,"msg":"操作成功"})

"""
  测试用例：删除
"""
@csrf_exempt
@require_http_methods(["GET"])
def del_testcase(request):
    try:
        rep = request.GET
        testcase_id = rep["case_id"]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"缺陷ID不能为空"})


    is_check_testcase = TestCase.objects.filter(case_id=testcase_id).values_list("isDelete")
    if len(is_check_testcase) == 0:
        return JsonResponse({"status":20004,"msg":"该条记录不存在"})
    try:
        if is_check_testcase[0][0] == 1:
            return JsonResponse({"status":20001,"msg":"该条记录已被他人删除"})
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"异常错误，请联系管理员"})
        
    try:
        tc = TestCase.objects.get(case_id=testcase_id)
        tc.deleter_id = get_user_object(request)
        tc.delete_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tc.isDelete = 1
        tc.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"删除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"删除成功"})


"""
    修改测试用例
"""
@csrf_exempt
@require_http_methods(["POST"])
def edit(request):
    try:
        req = json.loads(request.body)
        testcase_id = req["case_id"]
        case_obj = TestCase.objects.get(case_id=testcase_id)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"用例ID不能为空,并且需有效"})

    if "DataInput" in req:
        case_obj.DataInput = req["DataInput"]
    if "precondition" in req:
        case_obj.precondition = req["precondition"]
    if "remark" in req:
        case_obj.remark = req["remark"]
    if "priority" in req:
        case_obj.priority = req["priority"]
    if "steps" in req:
        case_obj.steps = req["steps"]
    if "title" in req:
        case_obj.title = req["title"]
    if "expected_result" in req:
        case_obj.expected_result = req["expected_result"]
    if "category" in req:
        case_obj.category = req["category"]

    if "module_id" in req:
        if len(req["module_id"]) == 1:
            try:
                m1_id = ModuleA.objects.get(id=req["module_id"][0])
            except Exception as e:
                return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
            else:
                case_obj.m1_id = m1_id
        if len(req["module_id"]) == 2:      
            try:
                m2_id = ModuleB.objects.get(id=req["module_id"][1])
            except Exception as e:
                return JsonResponse({"status": 40004, "msg": u"产品模块无效."})
            else:
                case_obj.m2_id = m2_id 

    try:
        change_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        case_obj.change_time = change_time
        case_obj.changer_id = get_user_object(request)
        case_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"修改失败"})
    else:
        # 保存附件
        try:
            if "annex" in req:
                annex = req["annex"]
                for f in annex:
                    aex = TestCaseFiles(
                        case_id = case_obj,
                        file_path = f
                        )
                    aex.save()
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"附件错误"})
        else:
            return JsonResponse({"status":20000,"msg":"修改成功"})

"""
  评审
"""
@csrf_exempt
@require_http_methods(["POST"])
def review(request):

    try:
        req = json.loads(request.body)
        case_id = req["case_id"]
        result = req["result"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"Result和case_id不能为空"})

    if result in [1,2]:
        pass
    else:
        return JsonResponse({"status":40001,"msg":"Result无效"})

    if "remark" in req:
        remark = req["remark"]
    else:
        remark = ""

    try:
        case_obj = TestCase.objects.get(case_id=case_id)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"case_id无效"})

    try:
        case_obj.isReview = result
        case_obj.save()

        review_result = TestCaseReview(
            user_id = get_user_object(request),
            case_id = case_obj,
            result = result,
            remark = remark
            )
        review_result.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"操作失败"})
    else:
        return JsonResponse({"status":20000,"msg":"操作成功"})

"""
  Testcase: 附件删除
"""
@csrf_exempt
@require_http_methods(["POST"])
def annex_delete(request):
    try:
        req = json.loads(request.body)
        file_path = req["file_path"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"文件路径不能为空哦"})
    
    try:
        file_obj = TestCaseFiles.objects.get(file_path=file_path)
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"没找到数据"})
    try:
        file_obj.isDelete = 1
        file_obj.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"附件删除失败"})
    else:
        return JsonResponse({"status":20000,"msg":"附件删除成功"})

"""
  bug export
"""
@require_http_methods(["GET"])
def export(request):

    q1 = Q()
    q1.connector = "AND"

    try:
        req = request.GET.dict()
        product_code = req["product_code"]
    except Exception as e:
        return JsonResponse({"status":40001,"msg":"产品名称不能为空"})
    else:
        q1.children.append(Q(**{"product_code":product_code}))

    if "m1_id" in req:
        m1_id = req["m1_id"]
        q1.children.append(Q(**{"m1_id":m1_id}))
    if "m2_id" in req:
        m1_id = req["m2_id"]
        q1.children.append(Q(**{"m2_id":m2_id}))

    test_data = TestCase.objects.filter(q1). \
        annotate(
            creator=F("creator_id__realname"),
            changer=F("changer_id__realname"),
            m1_name=F("m1_id__m1"),
            m2_name=F("m2_id__m2")
            ).\
        values_list("id","product_code","m1_name","m2_name","precondition",
            "title","steps","expected_result","DataInput","remark",
            "priority","status","m1_id","m2_id",
            "creator","changer","create_time","change_time","update_time")[:]

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
        filename = 'Case_{0}_{1}.xlsx'.format(product_code,visualtime)
        filepath = 'media/export/' + filename
        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet('TestCase')

        # 工作表头部
        header_name = ['id','产品','一级模块','二级模块','前置条件','用例标题','步骤','预期结果',
            '测试数据','备注','优先级','状态','m1_id','m2_id','创建者','修改人','创建时间','修改时间','最后更新时间']
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