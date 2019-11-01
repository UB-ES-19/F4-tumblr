# Create your models here.
from django.db import models

class Audio(models.Model):
    name=models.CharField(max_length=500)
    user=models.CharField(max_length=500)
    audiofile= models.FileField(upload_to='audios/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.audiofile)

class Chat(models.Model):
    # Template of video file, to change
    name=models.CharField(max_length=500)
    user=models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class Image(models.Model):
    name=models.CharField(max_length=500)
    user=models.CharField(max_length=500)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)

class Link(models.Model):
    # Template of video file, to change
    name= models.CharField(max_length=500)
    user=models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class Quote(models.Model):
    # Template of video file, to change
    name= models.CharField(max_length=500)
    user=models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class Text(models.Model):
    # Template of video file, to change
    name= models.CharField(max_length=500)
    user=models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class Video(models.Model):
    # Template of video file, to change
    name= models.CharField(max_length=500)
    user=models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)