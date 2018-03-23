from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import UserProfile,PasswordReset

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    remember = serializers.BooleanField(default=True, help_text = _("If checked you will stay logged in for 3 weeks"))

    def user_credentials(self, attrs):
        """
        Provides the credentials required to authenticate the user for login.
        """
        credentials = {}
        credentials["username"] = attrs["username"]
        credentials["password"] = attrs["password"]
        return credentials

    def validate(self, attrs):
        """ checks if login credentials are correct """
        user = authenticate(**self.user_credentials(attrs))

        if user:
            if user.is_active:
                self.instance = user
            else:
                raise serializers.ValidationError(_("This account is currently inactive."))
        else:
            error = _("Invalid login credentials.")
            raise serializers.ValidationError(error)
        return attrs
    

class UserCreateSerializer(serializers.ModelSerializer):
    """ Profile Serializer for User Creation """
    #password_confirmation = serializers.CharField(label=_('password_confirmation'))
    email = serializers.EmailField(source='profile_email',validators=[UniqueValidator(queryset=UserProfile.objects.all(),message="Email gia' presente")], write_only=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(),message="Username gia' presente")])
    password = serializers.CharField(allow_blank=False, write_only=True)
    password_confirmation = serializers.CharField(allow_blank=False, write_only=True)
    
    def create(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.user.email = attrs.get('user.email', instance.user.email)
            instance.poi = attrs.get('poi', instance.poi)
            instance.user.password = attrs.get('user.password', instance.user.password)
            return instance
        print attrs
        #user = attrs.get('user')
        password_confirmation = attrs.get('password_confirmation')
        password = attrs.get('password')
        if password != password_confirmation:
            message = {'password_confirmation': 'Password mismatch'}
            raise serializers.ValidationError(message)
        
        user = User.objects.create_user(username=attrs.get('username'), password=attrs.get('password'))
        u = UserProfile.objects.create(user=user,profile_email=attrs.get('profile_email'))
        message = "Benvenuto su Colibri\n"
        message += "Il tuo Username: %s  \n" % attrs.get('username')
        message += "La tua Password: %s  " % password
        print message
        send_mail("Benvenuto su CoLibri. I dettagli del tuo account", message, 'register@colibrisharing.net',[attrs.get('profile_email')])
        print u
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'username', 'email', 'password', 'password_confirmation',
        )
  
     
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        """ ensure email is in the database """
        #if EMAIL_CONFIRMATION:
        #    queryset = EmailAddress.objects.filter(email__iexact=value, verified=True)
        #else:
        queryset = UserProfile.objects.filter(profile_email__iexact=value)
        print queryset
        if queryset.count() < 1:
            raise serializers.ValidationError(_("Email non trovata"))
        return queryset.first().profile_email

    def create(self, validated_data):
        """ create password reset for user """
        return PasswordReset.objects.create_for_user(validated_data["email"])

      
class ResetPasswordKeySerializer(serializers.Serializer):
    password1 = serializers.CharField(help_text=_('New Password'),
                                      max_length=15)
    password2 = serializers.CharField(help_text=_('New Password (confirmation)'),
                                      max_length=15)

    def validate_password2(self, value):
        """ ensure password confirmation is correct """
        if value != self.initial_data['password1']:
            raise serializers.ValidationError(_('Password confirmation mismatch'))
        return value

    def update(self, instance, validated_data):
        """ change password """
        instance.user.set_password(validated_data["password1"])
        instance.user.full_clean()
        instance.user.save()
        # mark password reset object as reset
        instance.reset = True
        instance.full_clean()
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    """
    User profiles details
    """
    email = serializers.EmailField(source='profile_email',validators=[UniqueValidator(queryset=UserProfile.objects.all(),message="Email gia' presente")])
    username = serializers.CharField(source='user.username',read_only=True)

    #dove_sta = serializers.Field(source='where_is.username')
    
    class Meta:
        model = UserProfile
        
        fields= (
           'username','email','notify_wishlist','notify_added_books','phone','publish_phone','publish_email'
            )