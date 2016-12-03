from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^preguntas/$', views.preguntas, name='preguntas'),
    url(r'^graficos/$', views.graficos, name='graficos'),
]