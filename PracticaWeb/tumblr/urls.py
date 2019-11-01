from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login-email/$', views.check_email, name='login-email'),
    url(r'^audio_upload$', views.audio_upload, name='audio_upload'),
    url(r'^chat_upload$', views.chat_upload, name='chat_upload'),
    url(r'^image_upload$', views.image_upload, name='image_upload'),
    url(r'^link_upload$', views.link_upload, name='link_upload'),
    url(r'^quote_upload$', views.quote_upload, name='quote_upload'),
    url(r'^text_upload$', views.text_upload, name='text_upload'),
    url(r'^video_upload$', views.video_upload, name='video_upload'),
]