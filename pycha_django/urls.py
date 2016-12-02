from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^charts/colors', 'charts.views.colors_svg'),
    (r'^charts/', 'charts.views.index'),
)
