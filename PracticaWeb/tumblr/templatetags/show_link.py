# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('show/show_link.html')
def show_link(link, user, request):
    return {'link': link, 'user': user, 'request':request}