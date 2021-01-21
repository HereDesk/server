#!/usr/bin/env python
# wandali

"""
  数据分页(page)
"""
import requests
import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.models import User 
from app.models import Bug
from app.api.auth import get_user_object, get_user_name

def get_listing(req_data,data):
    
    try:
        pageSize = req_data['pageSize']
        pageNumber = req_data['pageNumber']
    except Exception as e:
        return JsonResponse({"status":40004,"msg":"缺少pageSize和pageNumber"})

    try:
        pageSize = int(pageSize)
        pageNumber = int(pageNumber)
    except Exception as e:
        return JsonResponse({"status":20004,"msg":"pageSize和pageNumber必须为整数"})
    else:
        if pageSize > 50:
            return JsonResponse({"status":20004,"msg":"做多一次只能请求50条数据哦"})
    try:
        paginator = Paginator(data, pageSize)
        contacts = paginator.page(pageNumber)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        return JsonResponse({"status":20001,"msg":u"别拉新了,我是有底线的"})
    else:
        return JsonResponse({"status":20000,"total":paginator.count,"data":list(contacts)})


class PushToDingDing(object):
    """推送钉钉消息
    """
    def __init__(self):
        self.dingding_url = "https://oapi.dingtalk.com/robot/send?access_token="

    def send_dingding(self, people, message):
        """发送钉钉消息
        """
        print("\n------dingding------\n", people, message)

        headers = {
            "Content-Type": "application/json"
        }
        content = {
            "msgtype": "text",
            "text": {
                "content": ""
            },
            "at": {
                "atMobiles": [],
                "isAtAll": False
            }
        }
        try:
            at_people = []
            at_people.append(people)
            content["at"]["atMobiles"] = at_people
            content["text"]["content"] = message
            res = requests.post(
                self.dingding_url,
                data=json.dumps(content),
                headers=headers
            )
            return res.text
        except Exception as e:
            print(e)
            return e

    def bug_push(self, http_request, assignedTo, bug_id):
        # 获取操作人员
        operator_name = get_user_name(http_request)
        # 获取手机号
        assignedTo_mobile = User.objects.filter(user_id=assignedTo).values_list("mobile",flat=True)[0]
        # 获取bug title和优先级
        bug_content = Bug.objects.filter(bug_id=bug_id).values('priority', "title")[0]

        if operator_name and assignedTo_mobile:
            bug_desc = "优先级: {0}\n内容: {1}".format(bug_content['priority'], bug_content['title'])
            msg = "【{0} 分配了一个Bug给你】\n{1}\n详情: http://192.168.12.201/app/qa/bug/deatils/?bug_id={2}".format(operator_name, bug_desc, bug_id)
            self.send_dingding(assignedTo_mobile, msg)