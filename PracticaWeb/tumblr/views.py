from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from tumblr.forms import SignUpForm
from .models import Audio, Chat, Image, Link, Quote, Text, Video
from .forms import AudioForm, ChatForm, ImageForm, LinkForm, QuoteForm, TextForm, VideoForm
from itertools import chain
from operator import attrgetter


def index(request):
    audio_form = AudioForm(request.POST or None, request.FILES or None)
    chat_form = ChatForm(request.POST or None, request.FILES or None)
    image_form = ImageForm(request.POST or None, request.FILES or None)
    link_form = LinkForm(request.POST or None, request.FILES or None)
    quote_form = QuoteForm(request.POST or None, request.FILES or None)
    text_form = TextForm(request.POST or None, request.FILES or None)
    video_form = VideoForm(request.POST or None, request.FILES or None)
    context = {'audio_form': audio_form,
               'chat_form': chat_form,
               'image_form': image_form,
               'link_form': link_form,
               'quote_form': quote_form,
               'text_form': text_form,
               'video_form': video_form}

    return render(request, 'templates/index.html', context)


def profile(request):
    audio_form = AudioForm(request.POST or None, request.FILES or None)
    chat_form = ChatForm(request.POST or None, request.FILES or None)
    image_form = ImageForm(request.POST or None, request.FILES or None)
    link_form = LinkForm(request.POST or None, request.FILES or None)
    quote_form = QuoteForm(request.POST or None, request.FILES or None)
    text_form = TextForm(request.POST or None, request.FILES or None)
    video_form = VideoForm(request.POST or None, request.FILES or None)
    audio_found = Audio.objects.filter(user=request.user.username)
    chat_found = Chat.objects.filter(user=request.user.username)
    image_found = Image.objects.filter(user=request.user.username)
    link_found = Link.objects.filter(user=request.user.username)
    quote_found = Quote.objects.filter(user=request.user.username)
    text_found = Text.objects.filter(user=request.user.username)
    video_found = Video.objects.filter(user=request.user.username)
    posts = sorted(chain(audio_found,
                         chat_found,
                         image_found,
                         link_found,
                         quote_found,
                         text_found,
                         video_found), key=attrgetter('timestamp'), reverse=True)
    context = {'audio_form': audio_form,
               'chat_form': chat_form,
               'image_form': image_form,
               'link_form': link_form,
               'quote_form': quote_form,
               'text_form': text_form,
               'video_form': video_form,
               'posts': posts}

    return render(request, 'templates/profile.html', context)


def audio_upload(request):
    audio_form = AudioForm(request.POST or None, request.FILES or None)
    if audio_form.is_valid():
        post = audio_form.save(commit=False)
        ext = str(post.audiofile)[len(str(post.audiofile))-3:]
        if ext == 'mp3':
            post.user = request.user
            post.save()
            audio_form = AudioForm(None, None)
        else:
            context = {'audio_form': audio_form}
            context['audio_type_error']= True
            return render(request, 'templates/index.html', context)
        # Return to page where we came from
        if "origin" in request.POST:
            origin = request.POST.get("origin")
            origin = origin if origin != "" else "/"
            return redirect(origin)
    context = {'audio_form': audio_form}
    return index(request)

def chat_upload(request):
    pass

def image_upload(request):
    image_form = ImageForm(request.POST or None, request.FILES or None)
    if image_form.is_valid():
        post = image_form.save(commit=False)
        ext = str(post.imagefile)[len(str(post.imagefile)) - 3:]
        if ext == 'jpg':
            post.user = request.user
            post.save()
            image_form = ImageForm(None, None)
        else:
            context = {'image_form': image_form}
            context['image_type_error'] = True
            return render(request, 'templates/index.html', context)
        # Return to page where we came from
        if "origin" in request.POST:
            origin = request.POST.get("origin")
            origin = origin if origin != "" else "/"
            return redirect(origin)
    context = {'image_form': image_form}
    return index(request)

def link_upload(request):
    pass

def quote_upload(request):
    if request.method == "POST":
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            quote = quote_form.save(commit=False)
            quote.user = request.user
            quote.save()
        # Return to page where we came from
        if "origin" in request.POST:
            origin = request.POST.get("origin")
            origin = origin if origin != "" else "/"
            return redirect(origin)
    context = {'quote_form': quote_form}
    return index(request)

def text_upload(request):
    pass

def video_upload(request):
    video_form = VideoForm(request.POST or None, request.FILES or None)
    if video_form.is_valid():
        post = video_form.save(commit=False)
        ext = str(post.videofile)[len(str(post.videofile))-3:]
        if ext == 'mp4':
            post.user = request.user
            post.save()
            video_form = VideoForm(None, None)
        else:
            context = {'video_form': video_form}
            context['video_type_error']= True
            return render(request, 'templates/index.html', context)
        # Return to page where we came from
        if "origin" in request.POST:
            origin = request.POST.get("origin")
            origin = origin if origin != "" else "/"
            return redirect(origin)
    context = {'video_form': video_form}
    return index(request)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data.get('email')
                User.objects.get(email=email)
                form = SignUpForm()
                return render(request, "registration/register.html", {
                    'form': form,
                    'mail_flag': True
                })
            except User.DoesNotExist:
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = SignUpForm()
    return render(request, "registration/register.html", {
        'form': form,
        'mail_flag': False
    })


def check_email(request):
    if request.method == 'POST':
        search_email = request.POST.get('email', None)
        try:
            User.objects.get(email=search_email)
            return HttpResponseRedirect(reverse("login"))
        except User.DoesNotExist:
            return HttpResponse("This email doesn't have a Dumblr account.")
    else:
        return render(request, "registration/login-email.html")
