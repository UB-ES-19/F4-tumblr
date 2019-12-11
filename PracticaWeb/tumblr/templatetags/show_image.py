# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('show/show_image.html')
def show_image(image_file, user, request):
    return {'image_file': image_file, 'user': user, 'request':request}