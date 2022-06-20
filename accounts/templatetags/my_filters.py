from django import template
from django.contrib.auth.models import Group


register = template.Library()

@register.filter(name='getkey')
def getkey(value, arg):
    return value[arg]

@register.filter()
def to_int(value):
   return int(value)

@register.filter
def is_negative(val):
    if abs(float(val))< 0:
        return True
    else:
        return False