# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-13 08:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0014_auto_20181113_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpiincidentreport',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 11, 13, 10, 2, 24, 262724)),
        ),
    ]
