from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.kpi_home_page, name='kpi_home_page'),
    url(r'^detail/(?P<incident_id>\d+)$', views.incident_detail, name='kpi_detail'),

    url(r'^eftleads/$', views.kpi_leads, name='kpi_leads'),
    url(r'^eftlead/(?P<eftlead_id>\d+)$', views.eftlead_detail, name='kpi_eftdetail'),

    url(r'^eftteam/(?P<eftteam_id>\d+)$', views.eftteam_detail, name='kpi_team'),
    url(r'^eftteams/$', views.kpi_teams, name='kpi_teams'),

    url(r'^company/(?P<company_id>\d+)$', views.kpi_company, name='kpi_company'),

    url(r'^help/$', views.kpi_help, name='kpi_help'),
]