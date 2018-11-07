#!/usr/bin/env python
# -*- coding:utf8 -*-
import json

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from django.db.models import F

from app.models import User
from app.models import Api
from app.models import ApiPermissions

from app.models import UserLog
from app.api.utils import get_listing

"""
    log列表
"""
@csrf_exempt
@require_http_methods(["GET"])
def userlog(request):
    data = UserLog.objects.all().\
        annotate(
            realname=F("user_id__realname")
        ).\
        values("id","ip","flag","realname","create_time","update_time")
    return HttpResponse(get_listing(request.GET, data))
