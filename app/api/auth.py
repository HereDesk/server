#!/usr/bin/env python

from django.http import JsonResponse
from app.models import User
from app.models import Authentication
from django.db.models import F

"""
  get token
"""
def get_token(request):
    token = ''
    if request.META.get('HTTP_AUTHORIZATION'):
        token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
    elif request.META.get('HTTP_AUTHENTICATION'):
        token = request.META['HTTP_AUTHENTICATION'].split(" ")[1]
    return token

"""
  get myinfo
"""
def get_myinfo(request):
    try:
        token = get_token(request)
        user = Authentication.objects.filter(token=token).\
            annotate(
                group=F('uid__group'),
                realname=F('uid__realname'),
                position=F('uid__position')
                ).\
            values('uid','group','realname','position')
        return list(user)[0]
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"服务器开小差了"})


"""
  get user objects
"""
def get_user_object(request):
    token = get_token(request)
    user = Authentication.objects.filter(token=token).values_list('uid',flat=True)[0]
    obj = User.objects.get(user_id=user)
    return obj

"""
  getuid
"""
def get_uid(request):
    token = get_token(request)
    user = Authentication.objects.filter(token=token).values_list('uid',flat=True)[0]
    return user

"""
  getusername
"""
def get_user_name(request):
    token = get_token(request)
    user = Authentication.objects.filter(token=token).values_list('uid__realname',flat=True)[0]
    return user

"""
  getusername
"""
def get_user_group(request):
    token = get_token(request)
    user = Authentication.objects.filter(token=token).values_list('uid__group',flat=True)[0]
    return user


"""
  权限检查
"""
def _auth(*args):
    def __auth(func):
        def _ischeck(request):
            token = get_token(request)
            try:
                user = Authentication.objects.filter(token=token).values_list('uid__group')
            except Exception as e:
                print(e)
                return JsonResponse({"status":40004,"msg":"异常错误"})
            for i in args:
                for g in i:
                    if user[0][0] == g:
                        return func(request)
                    else:
                        return JsonResponse({"status":14444,"msg":"无访问权限,请联系管理员"})
        return _ischeck
    return __auth