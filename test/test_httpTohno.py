#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '$Package_name'
__author__ = 'apple'
__mtime__ = '2016/11/19'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from django.test import TestCase

from console.models import sever_url_info
from httpTohno.httpTohnoUtils import httpTohnoUtils
from httpTohno.methodEnum import methodEnum
import json,sqlite3,os
from httpTohno.requestDict import requestDict


class TestHttpTohno(TestCase):

	def test_httpWithPost(self):
		#params = {"file": "/allen/allenFileName","content": "allenFileName_content","backupcount": 5,"syncfile": {"infos": [{"host": "192.168.250.178","file": "/home/allenFileName"}]}}
		params = {'file':'/allen/allenFileName'}
		httpTohnoWithPost = httpTohnoUtils(params,methodEnum.file_get)
		jsonData = httpTohnoWithPost.httpTohnoWithPost()
		print "JSON反馈信息=%s"%jsonData

	def test_httpWithGet(self):
		BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
		cx = sqlite3.connect(os.path.join(BASE_DIR,'.','consoleDb'))
		jsonData = httpTohnoUtils('', methodEnum.server_infos, r'dev').httpTohonWithGet()
		print 'jsonData=%s'%jsonData

	def test_methodEmum(self):
		print methodEnum.file_create

	def test_jsonData(self):
		jsonData = r'{"dir":"/","infos":[{"name":"erp","isdir":true},{"name":"kaokao","isdir":false},{"name":"qa","isdir":true}]}'
		dic = json.loads(jsonData)
		for key in dic:
			print dic[key]

	def test_requestDict(self):
		rd = requestDict().dirCreateDict('/erp')
		print type(rd)
		jsonData = json.dumps(rd)
		print type(jsonData)

	def test_sqlite(self):
		envObj = sever_url_info.objects.all()
		print type(envObj)


