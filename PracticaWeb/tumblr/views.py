from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login

from tumblr.forms import SignUpForm


def index(request):
    return render(request, 'templates/index.html')


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
            return HttpResponse("This email doesn't have a Tumblr account.")
    else:
        return render(request, "registration/login-email.html")