from django.conf.urls import url, include
from django.views.generic import TemplateView

from equipos import views
from equipos.views import *
from django.contrib.auth.decorators import login_required

from django.conf.urls import url


urlpatterns = [
### URLS Equipos ###
url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^equipos/$', views.equipo_list, name='equipo_list'),
    url(r'^equipos/create/$', views.equipo_create, name='equipo_create'),
    url(r'^equipos/(?P<pk>\d+)/update/$', views.equipo_update, name='equipo_update'),
    url(r'^equipos/(?P<pk>\d+)/delete/$', views.equipos_delete, name='equipo_delete'),
]
