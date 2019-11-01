from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Audio, Chat, Image, Link, Quote, Text, Video


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, label='', help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput(attrs={'class': "form-control" , 'placeholder':"email" }))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "form-control" , 'placeholder':"password" }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder':"repeat password" }))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"username" }))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'username')


class AudioForm(forms.ModelForm):
    class Meta:
        model= Audio
        fields= ["name", "audiofile"]

class ChatForm(forms.ModelForm):
    # Template from video form, to change
    class Meta:
        model= Chat
        fields= ["name", "videofile"]

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "imagefile"]

class LinkForm(forms.ModelForm):
    # Template from video form, to change
    class Meta:
        model= Video
        fields= ["name", "videofile"]

class QuoteForm(forms.ModelForm):
    # Template from video form, to change
    class Meta:
        model= Video
        fields= ["name", "videofile"]

class TextForm(forms.ModelForm):
    # Template from video form, to change
    class Meta:
        model= Video
        fields= ["name", "videofile"]

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]