from django.shortcuts import render
from .models import KPIIncidentReport, KPILead, KPITeam
from datatableview.views import XEditableDatatableView


class IncidentReportView(XEditableDatatableView):
    model = KPIIncidentReport
    datatable_options = {

    }


def kpi_home_page(request):
    context = dict()
    context['incidents'] = KPIIncidentReport.objects.all()
    return render(request, 'templates/index.html', context)


def incident_detail(request, incident_id):
    context = dict()
    context['incident'] = KPIIncidentReport.objects.get(pk=incident_id)
    return render(request, 'templates/incident_detail.html', context)


def kpi_leads(request):
    context = dict()
    context['leads'] = KPILead.objects.all()
    return render(request, 'templates/eftleads.html', context)


def kpi_teams(request):
    context = dict()
    context['teams'] = KPITeam.objects.all()
    return render(request, 'templates/eftteams.html', context)


def eftlead_detail(request, eftlead_id):
    context = dict()
    context['eftlead'] = KPILead.objects.get(pk=eftlead_id)
    context['team_names'] = KPITeam.objects.filter(eft_lead__id=eftlead_id)
    context['incidents'] = len(KPIIncidentReport.objects.filter(eft_lead__id=eftlead_id))
    return render(request, 'templates/eftlead.html', context)


def eftteam_detail(request, eftteam_id):
    context = dict()
    context['eftteam'] = KPITeam.objects.get(pk=eftteam_id)
    return render(request, 'templates/eftteam.html', context)


def kpi_company(request, company_id):
    context = dict()
    context['company'] = KPITeam.objects.get(pk=company_id)
    context['eftleads'] = KPILead.objects.filter(company__id=company_id)
    context['teams'] = KPITeam.objects.filter(company__id=company_id)
    context['incidents'] = KPIIncidentReport.objects.filter(company__id=company_id)
    return render(request, 'templates/eft_company.html', context)


def kpi_help(request):
    context = dict()
    return render(request, 'templates/help.html', context)