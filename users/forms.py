from django.contrib.auth.forms import UserCreationForm
from users.models import User
from catalog.forms import StyleForMexin

class UserRegisterForm(StyleForMexin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")