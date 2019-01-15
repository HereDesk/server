#!/usr/bin/env python

import os
import uuid
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

from app.models import Files
from app.models import User

@csrf_exempt
def upload(request):

    allow_suffix_list = [
        "jpg","png","jpeg","gif","bmp","svg","psd","tif","tga","ai",\
        "docx","docx","xls","xlsx","ppt","pptx","pdf","txt","log","md","html","json","ini","yaml",\
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
        return JsonResponse({"status":20000,"name":file_url})
