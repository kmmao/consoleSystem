# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0004_remove_templates_file_info_modify_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates_file_info',
            name='modify_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
