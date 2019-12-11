# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('show/show_audio.html')
def show_audio(audio_file, user, request):
    return {'audio_file': audio_file, 'user': user, 'request':request}