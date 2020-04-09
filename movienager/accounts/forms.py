from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.models import BaseModelForm

from accounts.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class UserEditForm(UserChangeForm):
    password = None
    exclude = ["email"]

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': 'readonly'})
            }
    
    def validate_unique(self):
        """
        Call the instance's validate_unique() method and update the form's
        validation errors if any were raised.
        """
        exclude = self._get_validation_exclusions()
        print(exclude)
        exclude.append("email")
        print(exclude)
        try:
            self.instance.validate_unique(exclude=exclude)
        except ValidationError as e:
            self._update_errors(e)

