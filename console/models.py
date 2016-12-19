#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class CompressedTextField(models.TextField):
    """
    model Fields for storing text in a compressed format (bz2 by default)
    """
    def from_db_value(self, value, expression, connection, context):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def to_python(self, value):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def get_prep_value(self, value):
        if not value:
            return value
        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                return value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value

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
    port = models.IntegerField()
    out_time = models.IntegerField()

#templates_file_info
class templates_file_info(models.Model):
    name = models.CharField(max_length=512)
    content = CompressedTextField()
    modify_by = models.CharField(max_length=64)
    modify_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])