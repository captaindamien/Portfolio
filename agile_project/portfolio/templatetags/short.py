from django import template

register = template.Library()

@register.filter
def shorter(value):
    return 'Password'