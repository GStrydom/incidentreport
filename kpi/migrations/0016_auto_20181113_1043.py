# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-13 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0015_auto_20181113_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpiincidentreport',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
