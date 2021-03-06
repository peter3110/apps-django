from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^data/$', views.data, name='data'),
]