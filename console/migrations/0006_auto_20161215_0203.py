# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0005_templates_file_info_modify_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sever_url_info',
            name='out_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sever_url_info',
            name='port',
            field=models.IntegerField(),
        ),
    ]
