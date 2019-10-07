from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login-email/$', views.check_email, name='login-email'),
    url(r'^accounts/login/$', views.login_mail, name='login'),
]