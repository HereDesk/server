#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hmac
import time
import base64
import os
from hashlib import md5
from hashlib import sha1

def p_encrypt(passwd,msg):
    return hmac.new(passwd.encode('utf-8'),msg.encode('utf-8'),sha1).hexdigest()

def generate_token():
	return base64.b64encode(os.urandom(150)).decode('ascii')

def generateId(msg):
	inputstr = str(time.time())
	return hmac.new(inputstr.encode('utf-8'),msg.encode('utf-8'),sha1).hexdigest()