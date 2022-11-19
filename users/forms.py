from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
