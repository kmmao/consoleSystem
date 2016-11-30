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

from console.models import sever_url_info
from httpTohno.methodEnum import methodEnum
import base64


class httpTohnoUtils:
	def __init__(self,params,method,env):
		self.params = params
		self.method = method
		self.env = env
		pass
	def httpTohonWithGet(self):
		httpClient = None
		try:
			severUrlInfo = sever_url_info.objects.get(name__exact=self.env)
			httpClient = httplib.HTTPConnection(severUrlInfo.url, int(severUrlInfo.port),
												timeout=int(severUrlInfo.out_time))
			httpClient.request('GET', self.method)

			# response是HTTPResponse对象
			response = httpClient.getresponse()
			jsonData = json.loads(response.read())
			if not jsonData["hostinfos"]:
				jsonData["hostinfos"] = []
			jsonData['status'] = response.status
			return jsonData
		except Exception, e:
			print e
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

			severUrlInfo = sever_url_info.objects.get(name__exact=self.env)
			httpClient = httplib.HTTPConnection(severUrlInfo.url, int(severUrlInfo.port), timeout=int(severUrlInfo.out_time))
			httpClient.request("POST", self.method, json.JSONEncoder().encode(self.params), headers)

			response = httpClient.getresponse()
			#print "状态=%s"%(response.status)
			#print "结果=%s"%(response.reason)
			#print response.read()
			#print "头信息=%s"%(response.getheaders())  # 获取头信息
			jsonData = json.loads(response.read())
			print 'response.read=%s'%jsonData
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
			print 'fainl jsonData=%s'%json.dumps(jsonData)
			return json.dumps(jsonData)
		except Exception, e:
			print 'httpTohnoWithPost-exception=%s'%e
		finally:
			if httpClient:
				httpClient.close()
