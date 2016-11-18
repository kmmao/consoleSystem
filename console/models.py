from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=20, default='a')

class userinfo(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    companyCode = models.CharField(max_length=64)