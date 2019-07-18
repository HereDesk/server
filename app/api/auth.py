#!/usr/bin/env python

from django.http import JsonResponse
from django.db.models import F
from django.db.models import Q

from app.models import User
from app.models import Authentication
from app.models import ProductMembers


"""
  getusername
"""
def is_admin(request):
    token = get_token(request)
    user = Authentication.objects.\
        filter(
            Q(token=token) &
            Q(uid__identity=0)).\
        values_list("uid")
    if len(user) == 1:
        return True
    else:
        return False

"""
  get token
"""
def get_token(request):
    token = ""
    if request.META.get("HTTP_AUTHORIZATION"):
        token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
    elif request.META.get("HTTP_AUTHENTICATION"):
        token = request.META["HTTP_AUTHENTICATION"].split(" ")[1]
    elif "token" in request.COOKIES:
        token = request.COOKIES["token"]
    return token

"""
  get myinfo
"""
def get_myinfo(request):
    token = get_token(request)
    user = Authentication.objects.filter(token=token).\
        annotate(
            username=F("uid__username"),
            realname=F("uid__realname"),
            position=F("uid__position"),
            identity=F("uid__identity")
            ).\
        values("uid","username","realname","position","identity")
    return list(user)[0]


"""
  get user objects
"""
def get_user_object(request):
    token = get_token(request)
    user = Authentication.objects.filter(token=token).values_list("uid",flat=True)[0]
    obj = User.objects.get(user_id=user)
    return obj

"""
  getuid
"""
def get_uid(request):
    token = get_token(request)
    user = Authentication.objects.filter(token=token).values_list("uid",flat=True)[0]
    return user

"""
  getusername
"""
def get_user_name(request):
    token = get_token(request)
    user = Authentication.objects.filter(token=token).values_list("uid__realname",flat=True)[0]
    return user

"""
  getusername
"""
def get_prdocut_user_role(request,product_id):
    try:
        token = get_token(request)
        uid = Authentication.objects.filter(token=token).values_list("uid",flat=True)[0]
        role = ProductMembers.objects.\
            filter(Q(members_id=uid) & Q(product_id=product_id)).\
            values_list("user_role",flat=True)[0]
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"获取用户项目权限错误"})
    else:
        print("--------------+++++++",role)
        return role


"""
  权限检查
"""
# def _auth(*args):
#     def __auth(func):
#         def _ischeck(request):
#             token = get_token(request)
#             try:
#                 user = Authentication.objects.filter(token=token).values_list("uid__group")
#             except Exception as e:
#                 print(e)
#                 return JsonResponse({"status":40004,"msg":"异常错误"})
#             for i in args:
#                 for g in i:
#                     if user[0][0] == g:
#                         return func(request)
#                     else:
#                         return JsonResponse({"status":14444,"msg":"无访问权限,请联系管理员"})
#         return _ischeck
#     return __auth
