from django import forms

from .models import KPICompany, KPILead, KPITeam


class IncidentForm(forms.Form):
    date        = forms.DateField()
    ir_num      = forms.CharField(max_length=20)
    company     = forms.ModelChoiceField(queryset=KPICompany.objects.all())
    team_name   = forms.ModelChoiceField(queryset=KPITeam.objects.all())
    eft_lead    = forms.ModelChoiceField(queryset=KPILead.objects.all())
    incident    = forms.CharField(max_length=10)
    description = forms.CharField(
                    max_length=2000,
                    widget=forms.Textarea(),
                    help_text="Enter description..."
                )
    hours_deducted = forms.IntegerField()
    reportable     = forms.BooleanField()
    reason         = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super(IncidentForm, self).clean()
        date = cleaned_data.get("date")
        ir_num = cleaned_data.get("ir_num")
        company = cleaned_data.get("company")
        team_name = cleaned_data.get("team_name")
        eft_lead = cleaned_data.get("eft_lead")
        incident = cleaned_data.get("incident")
        description = cleaned_data.get("description")
        hours_deducted = cleaned_data.get("hours_deducted")
        reportable = cleaned_data.get("reportable")
        reason = cleaned_data.get("reason")
