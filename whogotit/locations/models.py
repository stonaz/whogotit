# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField( _("Nome"),max_length=40,help_text=_("Nome"),blank=True,null=True)
    desc = models.CharField( _("Descrizione"),max_length=100,help_text=_("Descrizione"),blank=True,null=True)
    
    def __unicode__(self):
        return self.name
    
    
class Location(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    owner = models.ForeignKey(User,related_name='owner')
    name = models.CharField( _("Nome"),max_length=40,help_text=_("Nome"),blank=True,null=True)
    # The additional attributes we wish to include.
    coords = models.PointField(blank=True)
    address = models.CharField( _("Indirizzo"),max_length=100,help_text=_("Indirizzo"),blank=True,null=True)
    categories = models.ManyToManyField(Category)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name
    def username(self):
        return self.owner.username
# Create your models here.
