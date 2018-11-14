from django.shortcuts import render, redirect, get_object_or_404
from .models import KPIIncidentReport, KPILead, KPITeam, KPICompany
from datatableview.views import XEditableDatatableView
from .forms import IncidentForm


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
    context['companies'] = KPICompany.objects.all()
    context['leads'] = KPILead.objects.all()
    return render(request, 'templates/eftleads.html', context)


def kpi_teams(request):
    context = dict()
    context['companies'] = KPICompany.objects.all()
    context['teams'] = KPITeam.objects.all()
    return render(request, 'templates/eftteams.html', context)


def eftlead_detail(request, eftlead_id):
    context = dict()
    context['eftlead'] = KPILead.objects.get(pk=eftlead_id)
    context['team_names'] = KPITeam.objects.filter(eft_lead__id=eftlead_id)
    context['incidents'] = KPIIncidentReport.objects.filter(eft_lead__id=eftlead_id)
    return render(request, 'templates/eftlead.html', context)


def eftteam_detail(request, eftteam_id):
    context = dict()
    context['eftteam'] = KPITeam.objects.get(pk=eftteam_id)
    # context['eftleads'] = KPILead.objects.filter()!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    context['incidents'] = KPIIncidentReport.objects.filter(team_name__id=eftteam_id)
    return render(request, 'templates/eftteam.html', context)


def kpi_company(request, company_id):
    context = dict()
    context['company'] = KPITeam.objects.get(pk=company_id)
    context['eftleads'] = KPILead.objects.filter(company__id=company_id)
    context['teams'] = KPITeam.objects.filter(company__id=company_id)
    context['incidents'] = KPIIncidentReport.objects.filter(company__id=company_id)
    return render(request, 'templates/eft_company.html', context)


def kpi_create(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            print("Form is valid.")
            incident = KPIIncidentReport()
            incident.date = form.cleaned_data['date']
            incident.ir_num = form.cleaned_data['ir_num']
            incident.company = form.cleaned_data['company']
            incident.eft_lead = form.cleaned_data['eft_lead']
            incident.team_name = form.cleaned_data['team_name']
            incident.incident = form.cleaned_data['incident']
            incident.description = form.cleaned_data['description']
            incident.hours_deducted = form.cleaned_data['hours_deducted']
            incident.reportable = form.cleaned_data['reportable']
            incident.reason = form.cleaned_data['reason']
            incident.save()
            return redirect('kpi_home_page')
        else:
            print("Form is not valid.")

    else:
        form = IncidentForm()
    return render(request, 'templates/eftcreate.html', {'form': form})


def kpi_update(request, incident_id):
    incident = get_object_or_404(KPIIncidentReport, pk=incident_id)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('kpi_home_page')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'templates/eftcreate.html', {'form':form})


def kpi_delete(request, incident_id):
    incident = get_object_or_404(Book, pk=incident_id)    
    if request.method=='POST':
        book.delete()
        return redirect('kpi_home_page')
    return render(request, template_name, {'object':book})


def kpi_help(request):
    context = dict()
    return render(request, 'templates/help.html', context)