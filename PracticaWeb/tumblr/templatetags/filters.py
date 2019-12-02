from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter
@stringfilter
def remove_prefix(url):
    """Removes the http(s) prefix if the URL has one"""
    match = re.match(r"https?://(.*)", url)
    return match.group(1) if match else url

@register.filter
@stringfilter
def chat(chat):
    """Puts bold tags around character names in chat posts"""
    regex = re.compile(r"(.*?):")
    acc = []
    for line in chat.split("\n"):
        line = re.sub(regex, lambda match: "<span style=\"font-weight: bold;\">"+match.group(1)+":</span>", line)
        acc.append(line)
    return "\n".join(acc)