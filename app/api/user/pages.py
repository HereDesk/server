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

from app.api.auth import is_admin
from app.api.auth import get_uid

from app.models import ProductMembers


@csrf_exempt
@require_http_methods(["GET"])
def pages(request):

    admin_role = is_admin(request)

    if admin_role:
        return JsonResponse({"status": 20000, "msg": "该用户拥有所有权限"})
    else:

        # in the request, get product_id
        try:
            product_id = request.GET["product_id"]
            print(product_id)
        except Exception as e:
            return JsonResponse({"status":40001,"msg":"请求缺少项目ID"})

        try:
            uid = get_uid(request)
            user_product_role = None
            query_user_product_role = ProductMembers.objects.\
                filter(Q(product_id=product_id) & Q(member_id=uid) & Q(status=0)).\
                values("user_role")
            if len(query_user_product_role) == 0:
                return JsonResponse({"status":40004,"msg":"没有此项目的访问权限"})
        except Exception as e:
            print(e)
            return JsonResponse({"status":40001,"msg":"异常错误"})
        else:
            user_product_role = list(query_user_product_role)[0]["user_role"]

        try:
            data = PagesPermissions.objects.filter(Q(user_role=user_product_role)).\
                annotate(
                    url=F("page_id__page_url")
                ).\
                values("url","is_allow")
        except Exception as e:
            return JsonResponse({"status": 14444, "msg": u"查询异常错误，请联系管理员."})
        else:
            return JsonResponse({"status": 20000, "user_product_role":user_product_role,"data": list(data)})
