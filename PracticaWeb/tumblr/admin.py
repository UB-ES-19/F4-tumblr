from django.contrib import admin

# Register your models here.
from .models import Audio, Chat, Image, Link, Quote, Text, Video

admin.site.register(Audio)
admin.site.register(Chat)
admin.site.register(Image)
admin.site.register(Link)
admin.site.register(Quote)
admin.site.register(Text)
admin.site.register(Video)