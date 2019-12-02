# Inclusion tags relating to posts.
# See https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

from django import template

register = template.Library()

@register.inclusion_tag('posts/upload_text.html', takes_context=True)
def upload_text(context, form):
    return {'text_form': form, 'request': context['request']}
