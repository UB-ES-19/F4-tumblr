# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('posts/upload_video.html', takes_context=True)
def upload_video(context, form):
    return {'video_form': form, 'request': context['request']}
