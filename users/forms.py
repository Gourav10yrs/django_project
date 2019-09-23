from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# by default django gives user register form but, to add other fields
# we need to create a class that inherit UserCreationForm and add the other fields that we require.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Here Meta class gives nested name place for configuration and
    # keeps the configuration in one place and
    # the model is being effected would be User

    class Meta:
        model = User
        # fields here is the sequence we want in form and in what order.
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
