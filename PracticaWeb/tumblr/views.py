from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from tumblr.forms import SignUpForm
from .models import Audio, Chat, Image, Link, Quote, Text, Video, Follow, UserProfile
from .forms import AudioForm, ChatForm, ImageForm, LinkForm, QuoteForm, TextForm, VideoForm, UserProfile
from itertools import chain
from operator import attrgetter


def index(request, user_found=None):

    # Upload forms
    audio_form = AudioForm(request.POST or None, request.FILES or None)
    chat_form = ChatForm(request.POST or None, request.FILES or None)
    image_form = ImageForm(request.POST or None, request.FILES or None)
    link_form = LinkForm(request.POST or None, request.FILES or None)
    quote_form = QuoteForm(request.POST or None, request.FILES or None)
    text_form = TextForm(request.POST or None, request.FILES or None)
    video_form = VideoForm(request.POST or None, request.FILES or None)

    # Queries to display posts from people the user follows
    following = list_following(request) + [request.user.username]
    audio_found = Audio.objects.filter(user__in=following)
    chat_found = Chat.objects.filter(user__in=following)
    image_found = Image.objects.filter(user__in=following)
    link_found = Link.objects.filter(user__in=following)
    quote_found = Quote.objects.filter(user__in=following)
    text_found = Text.objects.filter(user__in=following)
    video_found = Video.objects.filter(user__in=following)

    posts = sorted(chain(
        audio_found,
        chat_found,
        image_found,
        link_found,
        quote_found,
        text_found,
        video_found
    ), key=attrgetter('timestamp'), reverse=True)

    get_pics(posts)

    context = {
        'audio_form': audio_form,
        'chat_form': chat_form,
        'image_form': image_form,
        'link_form': link_form,
        'quote_form': quote_form,
        'text_form': text_form,
        'video_form': video_form,
        'user_found': user_found,
        'posts': posts,
    }

    return render(request, 'templates/index.html', context)

def get_pics(posts):
    """gets the profile pircture url of the user who posted each post"""
    for post in posts:
        picture = UserProfile.objects.filter(username=post.user)[0].picture
        try:
            if picture.url is not None:
                post.user_picture = picture
        except:
            pass

def searched_profile(request, username=None):
    if request.user.username == username:
        return profile(request)
    else:
        audio_found = Audio.objects.filter(user=username)
        chat_found = Chat.objects.filter(user=username)
        image_found = Image.objects.filter(user=username)
        link_found = Link.objects.filter(user=username)
        quote_found = Quote.objects.filter(user=username)
        text_found = Text.objects.filter(user=username)
        video_found = Video.objects.filter(user=username)
        print(image_found)
        posts = sorted(chain(audio_found,
                             chat_found,
                             image_found,
                             link_found,
                             quote_found,
                             text_found,
                             video_found), key=attrgetter('timestamp'), reverse=True)
        get_pics(posts)
        context = {'posts': posts,
                   'searched_username': username,
                   'already_followed': already_following(request, username)}
        return render(request, 'templates/searched_profile.html', context)


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
    if request.method == "POST":
        chat_form = ChatForm(request.POST)
        if chat_form.is_valid():
            post = chat_form.save(commit=False)
            post.user = request.user
            post.save()

        if "origin" in request.POST:
            origin = request.POST.get("origin")
            origin = origin if origin != "" else "/"
            return redirect(origin)
    context = {'chat_form': chat_form}
    return index(request)

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
    if request.method == "POST":
        # link_form = LinkForm(request.POST or None, request.FILES or None)
        link_form = LinkForm(request.POST)
        if link_form.is_valid():
            post = link_form.save(commit=False)
            post.user = request.user
            post.save()

        if "origin" in request.POST:
            origin = request.POST.get("origin")
            origin = origin if origin != "" else "/"
            return redirect(origin)
    context = {'link_form': link_form}
    return index(request)

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
    if request.method == "POST":
        text_form = TextForm(request.POST)
        if text_form.is_valid():
            post = text_form.save(commit=False)
            post.user = request.user
            post.save()

        if "origin" in request.POST:
            origin = request.POST.get("origin")
            origin = origin if origin != "" else "/"
            return redirect(origin)
    context = {'text_form': text_form}
    return index(request)

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
                UserProfile.objects.get(email=email)
                form = SignUpForm()
                return render(request, "registration/register.html", {
                    'form': form,
                    'mail_flag': True
                })
            except UserProfile.DoesNotExist:
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
            user = UserProfile.objects.get(email=search_email)
            return HttpResponseRedirect(reverse("login") + "?username=" + user.username + "&email=" + search_email)
        except UserProfile.DoesNotExist:
            return HttpResponse("This email doesn't have a Dumblr account.")
    else:
        return render(request, "registration/login-email.html")

def list_following(request):
    connections = Follow.objects.filter(creator=request.user).values('following')
    usernames = []
    for i in connections:
        usernames.append(i['following'])
    return usernames

def list_users(request):
    name = request.GET.get('search', None)
    user_list = UserProfile.objects.filter(username__icontains=name)
    return profile_search(request, user_list)

def profile_search(request, user_found=None):
    context = {'user_found': user_found}
    return render(request, 'templates/profile_search.html', context)

def already_following(request, username):
    followed = list_following(request)
    return username in followed

def add_followed(request):
    username = request.GET.get('followed', None)
    new_follow = Follow(creator=request.user.username, following=username)
    new_follow.save()
    return searched_profile(request, username)


def remove_followed(request):
    username = request.GET.get('unfollowed', None)
    object = Follow.objects.filter(creator=request.user.username, following=username)
    object.delete()
    return searched_profile(request, username)