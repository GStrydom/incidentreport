from django import forms

from .models import KPIIncidentReport


class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = KPIIncidentReport
        fields = [
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