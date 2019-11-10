#!/usr/bin/env python

import os
import uuid
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

from app.models import Files
from app.models import User

from app.models import Bug
from app.models import BugAnnex
from app.models import TestCase
from app.models import TestCaseFiles

def save_file_info(data_type,req,url):
    try:
        if data_type == "bug":
            id = req["bug_id"]
            bug_obj = Bug.objects.get(bug_id=id)
            data = BugAnnex(bug_id=bug_obj,url=url)
            data.save()
        if data_type == "testcase":
            id = req["case_id"]
            case_obj = TestCase.objects.get(case_id=id)
            data = TestCaseFiles(case_id=case_obj,url=url)
            data.save()
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"服务器出小差了"})
    else:
        return JsonResponse({"status":20000,"msg":"附件保存成功","name":url})

@csrf_exempt
def upload(request):

    allow_suffix_list = [
        "jpg","png","jpeg","gif","bmp","svg","psd","tif","tga","ai",\
        "html","js","css","py","less","scss","styl","java","cpp",\
        "docx","docx","xls","xlsx","ppt","pptx","pdf","txt","log","md","json","ini","yaml",\
        "mp4","mp3","mov","m4v","wmv","ts","3gp","avi","flv","mkv","mpeg",
        "zip","rar","tar","7z","bz2","gz"]
    data_type = request.GET["type"]
    if data_type == "bug":
        path = "media/bug/"
    elif data_type == "testcase":
        path = "media/testcase/"
    else:
        path = "media/other/"

    try:
        original_filename = str(request.FILES.get("files"))
        suffix = str(original_filename.split(".")[-1]).lower()
        if suffix not in allow_suffix_list:
            return JsonResponse({"status":20004,"msg":"{0}文件不被允许, 若要上传, 请压缩后在上传！".format(suffix)})
    except Exception as e:
        print(e)
        return JsonResponse({"status":20004,"msg":"无法识别文件后缀"})

    file_content = request.FILES.get("files")

    try:
        filename = str(uuid.uuid4().hex) + "." + suffix
        with open(path+filename, "wb+") as destination:
            for chunk in file_content.chunks():
                destination.write(chunk)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"文件写入失败"})

    try:
        file_url = "/" + path+ filename
        data = Files(
            url = file_url,
            file_format = suffix,
            original_name = original_filename
            )
        data.save()
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"文件保存失败"})
    else:
        if data_type == "bug" and "bug_id" in request.GET:
            return save_file_info("bug",request.GET,file_url)
        elif data_type == "testcase" and "case_id" in request.GET:
            return save_file_info("testcase",request.GET,file_url)
        else:
            return JsonResponse({"status":20000,"msg":"附件保存成功","name":file_url})
