# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Audio(models.Model):
    user=models.CharField(max_length=500)
    audiofile= models.FileField(upload_to='audios/', null=True, verbose_name="")
    type = models.CharField(max_length=50, default='audio', editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.audiofile)

class Chat(models.Model): #mirar pull req
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, default='chat', editable=False)
    user = models.CharField(max_length=500)
    chat = models.TextField(max_length=200, default='')
    source = models.TextField(max_length=200, default='')

class Image(models.Model):
    user=models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, default='image', editable=False)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return str(self.imagefile)

class Link(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, default='link', editable=False)
    user = models.CharField(max_length=500)
    link = models.TextField(max_length=200, default='')
    source = models.TextField(max_length=200, default='')

class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, default='quote', editable=False)
    user = models.CharField(max_length=500)
    quote = models.TextField(max_length=200, default='')
    source = models.TextField(max_length=200, default='')

class Text(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, default='text', editable=False)
    user = models.CharField(max_length=500)
    text = models.TextField(max_length=200, default='')
    source = models.TextField(max_length=200, default='')

class Video(models.Model):
    # Template of video file, to change
    user=models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, default='video', editable=False)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return str(self.videofile)