#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'liukai'
__mtime__ = '2016/11/17'
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
import httplib,urllib



class test_httpClient(TestCase):
    def hello(self):
        print ("hello world")


    def httpClientForGetTest(self):
        httpClient = None

        try:
            httpClient = httplib.HTTPConnection('localhost', 8000, timeout=30)
            httpClient.request('GET', '/test')

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            print response.status
            print response.reason
            print response.read()
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()

    def httpClientForPost(self):
        httpClient = None
        try:
            params = urllib.urlencode({'name': 'tom', 'age': 22})
            headers = {"Content-type": "application/x-www-form-urlencoded"
                , "Accept": "text/plain"}

            httpClient = httplib.HTTPConnection("localhost", 8000, timeout=30)
            httpClient.request("POST", "/test", params, headers)

            response = httpClient.getresponse()
            print response.status
            print response.reason
            print response.read()
            print response.getheaders()  # 获取头信息
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()