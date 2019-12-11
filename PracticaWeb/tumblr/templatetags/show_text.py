# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('show/show_text.html')
def show_text(title, text, user, request):
    return {'title': title, 'text': text, 'user': user, 'request':request}