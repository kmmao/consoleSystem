# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0003_auto_20161130_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templates_file_info',
            name='modify_time',
        ),
    ]