# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-07 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0006_auto_20181107_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpiincidentreport',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 15, 36, 13, 196590)),
        ),
    ]
