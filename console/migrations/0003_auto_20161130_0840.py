# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0002_templates_file_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates_file_info',
            name='modify_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]