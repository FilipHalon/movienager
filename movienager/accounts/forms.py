from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.models import BaseModelForm

from accounts.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class UserEditForm(forms.ModelForm):
    password = forms.CharField(max_length=128, required=False)

    class Meta:
        model = User
        exclude = ('photo', 'last_login', 'date_joined', 'user_permissions', 'groups')
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': 'readonly'})
            }
    
    def clean(self):
        return self.cleaned_data


class UserExtendedEditForm(forms.ModelForm):
    class Meta(UserEditForm.Meta):
        exclude = ('last_login', 'groups', 'date_joined')

    def save(self):
        self.instance = super().save()
        self.instance.set_permission()
        return self.instance
