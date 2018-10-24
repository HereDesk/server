#!/usr/bin/env python
# -*- coding:utf8 -*-

from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.models import Authentication
from app.models import User
from app.models import Pages
from app.models import PagesPermissions

from app.api.auth import get_user_group

@csrf_exempt
@require_http_methods(["GET"])
def pages(request):

    user_group = get_user_group(request)

    try:
        data = PagesPermissions.objects.filter(Q(group=user_group)).\
            annotate(
                url=F("page_id__page_url")
            ).\
            values("url","is_allow")
    except Exception as e:
        return JsonResponse({"status": 14444, "msg": u"查询异常错误，请联系管理员."})
    else:
        return JsonResponse({"status": 20000, "data": list(data)})