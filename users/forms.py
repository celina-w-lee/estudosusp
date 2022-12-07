from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('name', 'nusp', 'email', 'password1', 'password2')

        