from django.contrib import admin

from .models import KPIIncidentReport, KPILead, KPITeam, KPICompany


admin.site.register(KPIIncidentReport)
admin.site.register(KPILead)
admin.site.register(KPITeam)
admin.site.register(KPICompany)

