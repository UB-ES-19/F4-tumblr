# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

'''
CAMBIAR A LA INFO QUE SE QUIERE PASAR 
'''
@register.inclusion_tag('show/show_video.html')
def show_video(image_file, request):
    return {'image_file': image_file, 'request':request}