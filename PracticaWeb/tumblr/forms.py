from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, label='', help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput(attrs={'class': "form-control" , 'placeholder':"email" }))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "form-control" , 'placeholder':"password" }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder':"repeat password" }))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"username" }))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'username')