from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Audio, Chat, Image, Link, Quote, Text, Video, UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, label='', help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput(attrs={'class': "form-control" , 'placeholder':"email" }))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "form-control" , 'placeholder':"password" }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder':"repeat password" }))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"username" }))

    class Meta:
        model = UserProfile
        fields = ('email', 'password1', 'password2', 'username')


class AudioForm(forms.ModelForm):
    audiofile = forms.FileField(label='', widget=forms.FileInput(attrs={'style': 'opacity: 0; height:270px; width: 100%'}))
    class Meta:
        model= Audio
        fields= ["audiofile"]

class ChatForm(forms.ModelForm):
    # Mirar al pull request
    class Meta:
        model= Chat
        fields= ["title", "chat"]

class ImageForm(forms.ModelForm):
    imagefile = forms.FileField(label='', widget=forms.FileInput(attrs={'style': 'opacity: 0; height:270px; width: 100%'}))
    class Meta:
        model= Image
        fields= ["imagefile"]

class LinkForm(forms.ModelForm):
    # Template from video form, to change
    class Meta:
        model= Link
        fields= ["link"]

class QuoteForm(forms.ModelForm):
    # Mirar al pull request
    class Meta:
        model= Quote
        fields= [ "quote", "source"]

class TextForm(forms.ModelForm):
    # Mirar al pull request
    class Meta:
        model= Text
        fields= ["title", "text"]

class VideoForm(forms.ModelForm):
    videofile = forms.FileField(label='', widget=forms.FileInput(attrs={'style': 'opacity: 0; height:270px; width: 100%'}))
    class Meta:
        model= Video
        fields= ["videofile"]