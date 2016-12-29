#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'apple'
__mtime__ = '2016/12/15'
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
import json
import urllib2


__metaclass = type


class HttpHelper:
	def __init__(self):
		pass

	name = 'http helper'
	# header
	__reqHeader = {}
	# url
	__reqUrl = ''
	# time
	__reqTimeOut = 30

	# 构建Get请求
	def __buildGetRequest(self):
		if len(self.__reqHeader) == 0:
			request = urllib2.Request(self.__reqUrl)
		else:
			request = urllib2.Request(self.__reqUrl, headers=self.__reqHeader)
		return request

	# 构建post,put,delete请求
	def __buildPostPutDeleteRequest(self, postData):
		if len(self.__reqHeader) == 0:
			request = urllib2.Request(self.__reqUrl, data=postData)
		else:
			request = urllib2.Request(self.__reqUrl, headers=self.__reqHeader, data=postData)
		return request

		# 添加header,默认传的是json

	def headers(self, headers={'Content-Type': 'application/json'}):
		'''
			{'Content-Type': 'application/json'}
			application/xml ：在 XML RPC，如 RESTful/SOAP 调用时使用
			application/json ：在 JSON RPC 调用时使用
			application/x-www-form-urlencoded ：浏览器提交 Web 表单时使用
		'''
		self.__reqHeader = headers
		return self

	# 添加url
	def url(self, url):
		print url
		self.__reqUrl = url
		return self

	# 添加超时
	def timeOut(self, time):
		self.__reqTimeOut = time
		return self

	# 是否debug
	def debug(self):
		httpHandler = urllib2.HTTPHandler(debuglevel=1)
		httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
		opener = urllib2.build_opener(httpHandler, httpsHandler)
		urllib2.install_opener(opener)
		return self

	# 处理response
	def __handleResponse(self, request):
		try:
			if self.__reqTimeOut == 0:
				res = urllib2.urlopen(request)
			else:
				res = urllib2.urlopen(request, timeout=self.__reqTimeOut)
			return res.read()
		except urllib2.HTTPError, e:
			print e.code
			return e.read()

	# get请求
	def get(self):
		request = self.__buildGetRequest()
		return self.__handleResponse(request)

	# post请求
	def post(self, postData):
		request = self.__buildPostPutDeleteRequest(postData=postData)
		return self.__handleResponse(request)

	# put请求
	def put(self, putData):
		request = self.__buildPostPutDeleteRequest(postData=putData)
		request.get_method = lambda: 'PUT'
		return self.__handleResponse(request)

	# delete请求
	def delete(self, putData):
		request = self.__buildPostPutDeleteRequest(postData=putData)
		request.get_method = lambda: 'DELETE'
		return self.__handleResponse(request)

if __name__ == '__main__':
	def getData(data):
			print data

	httpHelper = HttpHelper()
	url_shiva = 'http://127.0.0.1:5000/templateFile/1'
	# 简单的get请求
	httpHelper.url(url=url_shiva).get()
	# post请求
	# httpHelper.debug() \
	# 	.url(url_shiva) \
	# 	.headers() \
	# 	.post(postData=json.dumps({'id':1}),func=getData)
