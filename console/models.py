from __future__ import unicode_literals

from django.db import models

#student for test
class Student(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=20, default='a')

#user info
class user_info(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    company_code = models.CharField(max_length=64)

#server url info
class sever_url_info(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    default_path = models.CharField(max_length=64)
    port = models.CharField(max_length=64)
    out_time = models.CharField(max_length=64)