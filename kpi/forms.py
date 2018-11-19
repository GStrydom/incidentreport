from django import forms

from .models import KPICompany, KPILead, KPITeam, KPIIncidentReport


class IReportForm(forms.ModelForm):
    class Meta:
        model = KPIIncidentReport
        fields = [
            'date',
            'ir_num',
            'company',
            'eft_lead',
            'team_name',
            'incident',
            'description',
            'hours_deducted',
            'reportable',
            'reason'
        ]
