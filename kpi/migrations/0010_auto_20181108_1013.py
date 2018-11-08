# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-08 08:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0009_auto_20181108_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpiincidentreport',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 8, 10, 13, 13, 187906)),
        ),
        migrations.AlterField(
            model_name='kpilead',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kpi.KPICompany'),
        ),
    ]