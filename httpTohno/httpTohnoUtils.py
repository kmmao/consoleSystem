#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '死去的猫儿'
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
import httplib,json
import logging

from console.models import sever_url_info
from httpTohno.methodEnum import methodEnum
import base64
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger('httpTohno')


class httpTohnoUtils:
	def __init__(self,params,method,env,url='localhost',port=5000,out_time=30):
		self.params = params
		self.method = method
		self.env = env
		self.url = url
		self.port = port
		self.out_time = out_time
		pass
	def httpTohonWithGet(self):
		httpClient = None
		try:
			httpClient = httplib.HTTPConnection(self.url, self.port,timeout=self.out_time)
			httpClient.request('GET', self.method)

			# response是HTTPResponse对象
			response = httpClient.getresponse()
			if self.env == 'shiva':
				return json.loads(response.read())
			jsonData = json.loads(response.read())
			if not jsonData["hostinfos"]:
				jsonData["hostinfos"] = []
			jsonData['status'] = response.status
			return jsonData
		except Exception, e:
			logger.error('httpTohonWithGet：%s' % e)
		finally:
			if httpClient:
				httpClient.close()

	def httpTohnoWithPost(self):
		"""
		:param method: action name ex: /dir?action=scan
		:param params: json string ex:{"dir": "/"}
		"""
		httpClient = None
		try:
			headers = {'Content-Type': 'application/json'}
			httpClient = httplib.HTTPConnection(self.url, self.port, timeout=self.out_time)
			httpClient.request("POST", self.method, json.JSONEncoder().encode(self.params), headers)
			logger.info('request data = %s' % json.JSONEncoder().encode(self.params))
			response = httpClient.getresponse()
			#print "状态=%s"%(response.status)
			#print "结果=%s"%(response.reason)
			#print response.read()
			#print "头信息=%s"%(response.getheaders())  # 获取头信息
			if self.env == 'shiva':
				return json.loads(response.read())
			jsonData = json.loads(response.read())
			logger.info('response.read = %s' % jsonData)
			#500错误
			# if jsonData.status == 500:
			# 	return json.dumps(jsonData)
			if(self.method == methodEnum.dir_scan):
				if not jsonData["infos"] :
					jsonData["infos"] = []
			if(self.method == methodEnum.file_get or self.method == methodEnum.file_backupget):
				if jsonData['content'] != '':
					jsonData['content'] = base64.b64decode(jsonData['content'])
			jsonData['status'] = response.status
			logger.info('fainl jsonData = %s' % json.dumps(jsonData))
			return json.dumps(jsonData)
		except Exception, e:
			print e
			logger.error('httpTohnoWithPost-exception=%s' % e)
		finally:
			if httpClient:
				httpClient.close()
