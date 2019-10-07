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
    })


def check_email(request):
    if request.method == 'POST':
        search_email = request.POST.get('email', None)
        # No troba usuaris, cal canviar el model de dades
        if len(User.objects.filter(email=search_email)):
            request.method = 'GET'
            return login_mail(request)
        else:
            return HttpResponse("This email doesn't have a Tumblr account.")
    else:
        return render(request, "registration/login-email.html")


def login_mail(request):
    if request.method == 'POST':
        search_email = request.POST.get('email', None)
        if len(User.objects.filter(email=search_email)):
            user = User.objects.filter(email=search_email)
            # Aconseguir el username del mail
            # provar login amb username i contrasenya
    else:
        return HttpResponseRedirect(reverse("login"))