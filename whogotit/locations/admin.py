# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin
from models import Location,Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Location, admin.OSMGeoAdmin)

