# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
from .models import UserProfile
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.conf import settings

def now():
    """ returns the current date and time in UTC format (datetime object) """
    return datetime.utcnow().replace(tzinfo=utc)

def create_profile(strategy, details, response, user, *args, **kwargs):
    print details['email']
    # username = kwargs['details']['username']
    # user_object = User.objects.get(username=username)
    if UserProfile.objects.filter(user=user).exists():
        pass
    else:
        new_profile = UserProfile(user=user,profile_email=details['email'])
        try:
            new_profile.save()
        except Exception:
                SITE_URL = settings.SITE_URL
                return render_to_response(
            'angular/duplicate_mail.html', {'SITE_URL':SITE_URL})
      
    return kwargs

