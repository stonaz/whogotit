from __future__ import absolute_import

from django.contrib.auth.models import User
from profiles.models import UserProfile

def run():
    users=User.objects.all()
    for user in users:
        if user.is_superuser != True:
            print user
            profile = UserProfile.objects.get(user=user)
            print user.email
            print profile.profile_email
            profile.profile_email = user.email
            profile.save()
            print user.email
    
    

