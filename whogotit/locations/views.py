# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics, permissions, authentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Location,Category
from .serializers import *
from .permissions import IsOwnerOrReadOnly,IsOwner
# Create your views here.

class CategoryLocationsView(generics.ListAPIView):
    """
    ### GET
    
    Retrieve Categories.
        
    """
    
    authentication_classes = (SessionAuthentication,)
    serializer_class = CategoryLocationsSerializer
    model = Category
    queryset = Category.objects.all()   

category_locations = CategoryLocationsView.as_view()


class HyperLinkLocationList(generics.ListAPIView):
    """
    ### GET
    
    Retrieve locations.
        
    """
    
    authentication_classes = (SessionAuthentication,)
    serializer_class = HyperlinkLocationSerializer
    model = Location
    queryset = Location.objects.all()   

hyperlinklist = HyperLinkLocationList.as_view()

class Locations(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve locations.
        
    """
    
    authentication_classes = (SessionAuthentication,)
    serializer_class = ListLocationSerializer
    model = Location
    queryset = Location.objects.all()   

locations = Locations.as_view()

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

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    ### GET
    
    Retrieve details of Location
        
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly )
    authentication_classes = (SessionAuthentication,)
    serializer_class= LocationSerializer
    model=Location
    
    def get_queryset(self):
        #user = self.kwargs.get('user', None)
        location_id = self.kwargs.get('pk', None)
        # try:
        #     user_id=User.objects.get(username=user)
        # except Exception:
        #     raise Http404(_('Not found'))
        return Location.objects.all().filter(id=location_id)

location_detail = LocationDetail.as_view()