#!/usr/bin/env python

import os
import uuid
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload(request):
    img = request.FILES.get('images')
    if img:
        filename = uuid.uuid4().hex
        try:
            fileinfo = uuid.uuid4().hex
        except Exception as e:
            return JsonResponse({"status":20004,"msg":"服务器出错了，无法保存文件"})
        with open('media/bug/'+fileinfo, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        return JsonResponse({"status":20000,"name":'/media/bug/'+ fileinfo})
    else:
        return JsonResponse({"status":20004,"msg":"无效文件名"})
