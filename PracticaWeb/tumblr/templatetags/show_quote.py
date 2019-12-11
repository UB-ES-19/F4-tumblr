# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('show/show_quote.html')
def show_quote(quote, source, user, request):
    return {'quote': quote, 'source': source, 'user': user, 'request':request}