# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-09 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_area_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='areas',
        ),
        migrations.RemoveField(
            model_name='location',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]