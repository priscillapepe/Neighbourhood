from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm,
                                       PasswordResetForm,
                                       SetPasswordForm
                                       )
from .models import Neighbourhood,Profile,Post,Business


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)


username = forms.CharField(widget=forms.TextInput(attrs={
    "class": "input",
    "type": "text",
    "placeholder": "enter username"
}))

password = forms.CharField(widget=forms.TextInput(attrs={
    "class": "input",
    "type": "password",
    "placeholder": "enter password"
}))


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter email-id"
    }))

class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter email-id"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "re-enter password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "password2"]

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')