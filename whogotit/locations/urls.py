from django.conf.urls import  include, url
from . import views


urlpatterns = [
    url(r'^$', views.location_list, name='location_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.location_detail, name='location_detail'),
    url(r'^list/$', views.locations, name='locations'),
    url(r'^hyperlinklist/$', views.hyperlinklist, name='hyperlinklist'),
    url(r'^categorylist/$', views.category_locations, name='category_locations'),
]

