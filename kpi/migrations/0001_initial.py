# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-30 07:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KPIIncidentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 10, 30, 9, 13, 13, 248619))),
                ('ir_num', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=100)),
                ('eft_lead', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
                ('incident', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('hours_deducted', models.IntegerField()),
                ('reportable', models.BooleanField(default=False)),
                ('reason', models.CharField(max_length=50)),
            ],
        ),
    ]