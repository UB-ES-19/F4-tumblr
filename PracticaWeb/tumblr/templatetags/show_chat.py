# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('show/show_chat.html')
def show_chat(title, chat, user, request):
    return {'title': title, 'chat': chat, 'user': user, 'request':request}
