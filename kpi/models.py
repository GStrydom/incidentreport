from django.db import models

import datetime


class KPICompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class KPILead(models.Model):
    name            = models.CharField(max_length=255)
    position        = models.CharField(max_length=255)
    company         = models.ForeignKey(KPICompany)
    profile_pic     = models.ImageField(upload_to='static/assets/img/profile_pics')

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
    eft_lead        = models.ForeignKey(KPILead)
    team_name       = models.ForeignKey(KPITeam)
    incident        = models.CharField(max_length=10)
    description     = models.CharField(max_length=255)
    hours_deducted  = models.IntegerField()
    reportable      = models.BooleanField(default=False)
    reason          = models.CharField(max_length=50)

    def __str__(self):
        return self.ir_num