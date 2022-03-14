from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.db.models import fields
from .models import Rater
from django.forms import ModelForm

class userForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Usename"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Email"
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Repeat-Password"
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class RaterForm(forms.ModelForm):
    # specify the name of model to use
    # Movie_Name = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "Movie Name"
    # }))
    # Genre = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "Genre"
    # }))
    # Directed_By = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "Directed By"
    # }))
    # Description = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "textarea",
    #     "placeholder": "Description"
    # }))
    class Meta:
        model = Rater
        fields = "__all__"