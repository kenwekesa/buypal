from django import template
from django.contrib.auth.models import Group


register = template.Library()

@register.filter(name='getkey')
def getkey(value, arg):
    return value[arg]