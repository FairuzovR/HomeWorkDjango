from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from catalog.forms import StyleForMexin
from django import forms


class UserRegisterForm(StyleForMexin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class ProfileForm(StyleForMexin, UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
