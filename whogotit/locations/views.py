# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Location
from .serializers import *
# Create your views here.
class LocationList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve locations.
        
    """
    
    authentication_classes = (SessionAuthentication,)
    serializer_class = LocationSerializer
    model = Location
    queryset = Location.objects.all()   

location_list = LocationList.as_view()