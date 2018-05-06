from django.conf.urls import  include, url
from . import views


urlpatterns = [
    url(r'^locations/$', views.location_list, name='location_list'),
]

