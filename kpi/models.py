from django.db import models
from smart_selects.db_fields import ChainedForeignKey


import datetime


class KPICompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class KPILead(models.Model):
    name            = models.CharField(max_length=255)
    position        = models.CharField(max_length=255)
    company         = models.ForeignKey(KPICompany)
    profile_pic     = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.name


class KPITeam(models.Model):
    name            = models.CharField(max_length=100)
    eft_lead        = models.ForeignKey(KPILead)
    company         = models.ForeignKey(KPICompany)

    def __str__(self):
        return self.name


class KPIIncidentReport(models.Model):
    date            = models.CharField(max_length=20)
    ir_num          = models.CharField(max_length=10)
    company         = models.ForeignKey(KPICompany)
    eft_lead        = ChainedForeignKey(
                        KPILead,
                        chained_field='company',
                        chained_model_field='company',
                        show_all=False,
                        auto_choose=True,
                        sort=True
                    )
    team_name       = ChainedForeignKey(
                        KPITeam,
                        chained_field='eft_lead',
                        chained_model_field='eft_lead',
                        show_all=False,
                        auto_choose=True,
                        sort=True
                    )
    incident        = models.CharField(max_length=10)
    description     = models.CharField(max_length=255)
    hours_deducted  = models.IntegerField()
    reportable      = models.NullBooleanField(null=True)
    reason          = models.CharField(max_length=50)

    def __str__(self):
        return self.ir_num