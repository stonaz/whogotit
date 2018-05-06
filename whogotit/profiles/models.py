from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _
from django.utils.http import int_to_base36
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator as token_generator

from django.conf import settings
from email_null import EmailNullField

def now():
    """ returns the current date and time in UTC format (datetime object) """
    return datetime.utcnow().replace(tzinfo=utc)

#def get_user_email(user):
#    print type( user)
#    u = User.objects.get(id= user)
#    email =u.email
#    return email


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    # The additional attributes we wish to include.
    profile_email = EmailNullField(blank=True, null=True,unique=True)
    phone = models.CharField( _("Telefono"),max_length=20,help_text=_("Telefono"),blank=True,null=True)
    publish_phone = models.BooleanField(default=False)
    publish_email = models.BooleanField(default=True)
    notify_wishlist = models.BooleanField(default=False)
    notify_added_books = models.BooleanField(default=False)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    
  
    
class PasswordResetManager(models.Manager):
    """ Password Reset Manager """

    def create_for_user(self, user):
        """ create password reset for specified user """
        # support passing email address too
        if type(user) is unicode:
            userprofile = UserProfile.objects.get(profile_email=user)
            user = User.objects.get(id=userprofile.user_id)

        temp_key = token_generator.make_token(user)

        # save it to the password reset model
        password_reset = PasswordReset(user=user, temp_key=temp_key)
        password_reset.save()
        print user.id
        print int_to_base36(5000)
        # send the password reset email
        subject = _("Password reset email sent")
        message = render_to_string("profiles/email_messages/password_reset_key_message.txt", {
            "user": user,
            "uid": int_to_base36(user.id),
            "temp_key": temp_key,
            "site_url": settings.SITE_URL,
            "site_name": settings.SITE_NAME
        })
        print message
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [userprofile.profile_email])

        return password_reset


class PasswordReset(models.Model):
    """
    Password reset Key
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"))

    temp_key = models.CharField(_("temp_key"), max_length=100)
    timestamp = models.DateTimeField(_("timestamp"), default=now)
    reset = models.BooleanField(_("reset yet?"), default=False)

    objects = PasswordResetManager()

    class Meta:
        verbose_name = _('password reset')
        verbose_name_plural = _('password resets')
        app_label = 'profiles'

    def __unicode__(self):
        return "%s (key=%s, reset=%r)" % (
            self.user.username,
            self.temp_key,
            self.reset
        )
