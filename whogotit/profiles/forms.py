from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from .models import PasswordReset

__all__ = [
    'ResetPasswordForm',
    'ResetPasswordKeyForm'
]

class ResetPasswordKeyForm(forms.Form):
    error_css_class = 'errorlist'
    password1 = forms.CharField(
        label=_("Nuova Password"),
        widget=forms.PasswordInput(render_value=False)
    )
    password2 = forms.CharField(
        label=_("Nuova Password (ripeti)"),
        widget=forms.PasswordInput(render_value=False)
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.temp_key = kwargs.pop("temp_key", None)
        super(ResetPasswordKeyForm, self).__init__(*args, **kwargs)

    def clean_password2(self):
        if "password1" in self.cleaned_data and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
                raise forms.ValidationError(_("Le passwords inserite non sono uguali"))
        return self.cleaned_data["password2"]

    def save(self):
        # set the new user password
        user = self.user
        user.set_password(self.cleaned_data["password1"])
        user.save()
        # mark password reset object as reset
        PasswordReset.objects.filter(temp_key=self.temp_key).update(reset=True)