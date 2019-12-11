# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('show/show_video.html')
def show_video(video_file, user, request):
    return {'video_file': video_file, 'user': user, 'request':request}