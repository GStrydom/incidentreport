from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView


urlpatterns = [
	url(r'^$', RedirectView.as_view(url='accounts/login'), name='site_home'),
    url(r'^admin/', admin.site.urls),
    url(r'^kpi/', include('kpi.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
