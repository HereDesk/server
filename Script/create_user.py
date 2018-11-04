#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import re
import time
import json
import uuid
import string
import random
import pymysql
import hmac
import base64
from hashlib import md5
from hashlib import sha1

email = input("\n -> please input email: ")

# check email
re_mail=r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
if re.match(re_mail,email):
  pass
else:
  print("\n -> email input error.")
  sys.exit()

team_name = input("\n -> please input team name:")

# connect mysql 
mysql_user = input("\n -> please input Mysql user: ")
mysql_passwd = input("\n -> please input Mysql password: ")
try:
	db = pymysql.Connect(
	    host='127.0.0.1',
	    port=3306,
	    user=mysql_user,
	    passwd=mysql_passwd,
	    db='here_desk',
	    charset='utf8')
	cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
except Exception as e:
	print(e)
	print('-->: Mysql Connect Error.')
	sys.exit()

# general data
def p_encrypt(passwd,msg):
    return hmac.new(passwd.encode('utf-8'),msg.encode('utf-8'),sha1).hexdigest()


curremt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
team_id = ''.join(str(uuid.uuid4()).split('-'))
team_sql = "insert into `t_team` ( `id`, `team_name`,`create_time`, `update_time`) \
    values ( '{0}', '{1}','{2}', '{3}');".format(team_id,team_name,curremt_time,curremt_time)


uid = str(uuid.uuid4())    
suid = ''.join(uid.split('-'))
token = base64.b64encode(os.urandom(150)).decode('ascii')
passwd = ''.join(random.sample(string.ascii_letters + string.digits, 8))
encrypt_passwd = p_encrypt(passwd,email)


# sql
user_sql = "insert into `t_user` ( `user_id`, `email`, `password`, `mobile`, `user_status`,\
    `realname`, `position`, `gender`, `avatarUrl`, `province`, `city`, `source`, `create_time`,\
    `update_time`, `group`,`team_id`,`identity`) values ( '{0}', '{1}', '{2}', null, '1', '超级管理员', null, '1',\
    null, null, null, null, '{3}', '{4}', 'admin','{5}','{6}');".\
    format(suid,email,encrypt_passwd,curremt_time,curremt_time,team_id,0)
token_sql = "insert into `t_authentication` ( `token`, `uid`) values ( '{0}', '{1}');".format(token,suid)

# team
try:
  cursor = db.cursor()
  cursor.execute(team_sql)
except Exception as e:
  print(e)
else:
  db.commit()

# user
try:
  cursor = db.cursor()
  cursor.execute(user_sql)
  cursor.execute(token_sql)
except Exception as e:
  print(e)
else:
  db.commit()
  print('\n ->:Success. New user passwd:',passwd)