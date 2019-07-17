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

email = input("\n -> please input admin email: ")

# check email
re_mail=r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
if re.match(re_mail,email):
  pass
else:
  print("\n -> admin email input error.")
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
	    db='hdesk',
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
uid = str(uuid.uuid4())
suid = ''.join(uid.split('-'))
token = base64.b64encode(os.urandom(150)).decode('ascii')
passwd = ''.join(random.sample(string.ascii_letters + string.digits, 8))
encrypt_passwd = p_encrypt(passwd,email)


# sql
user_sql = "insert into `user` ( `user_id`, `email`, `password`, `mobile`, `user_status`,\
    `realname`, `position`, `gender`, `avatarUrl`, `province`, `city`, `source`, `create_time`,\
    `update_time`,`identity`,`username`) values ( '{0}', '{1}', '{2}', null, '1', '超级管理员', null, '1',\
    null, null, null, null, '{3}', '{4}','{5}','admin');".\
    format(suid,email,encrypt_passwd,curremt_time,curremt_time,0)
token_sql = "insert into `user_authentication` ( `token`, `uid`,`create_time`, `update_time`) values ( '{0}', '{1}','{2}','{3}');".format(token,suid,curremt_time,curremt_time)

# user
print("\n -> update user to db...")
try:
  cursor = db.cursor()
  cursor.execute(user_sql)
  cursor.execute(token_sql)
except Exception as e:
  print(e)
else:
  db.commit()
  print('\n ->:Success. New user passwd:',passwd)

# team
team_id = ''.join(str(uuid.uuid4()).split('-'))
team_sql = "insert into `team` ( `id`, `team_name`,`create_time`, `update_time`, `creator_id`) \
    values ( '{0}', '{1}','{2}', '{3}','{4}');".format(team_id,team_name,curremt_time,curremt_time,suid)

# team
print("\n -> update team to db...")
try:
  cursor = db.cursor()
  cursor.execute(team_sql)
except Exception as e:
  print(e)
else:
  db.commit()

# team member
team_members_sql = "insert into `team_members` (`status`,`join_time`,`team_id`,`user_id`,`update_time`) \
    values ('0','{0}', '{1}','{2}','{3}');".format(curremt_time,team_id,suid,curremt_time)

# team
print("\n -> update team member to db...")
try:
  cursor = db.cursor()
  cursor.execute(team_members_sql)
except Exception as e:
  print(e)
else:
  db.commit()
