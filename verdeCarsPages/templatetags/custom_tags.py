from django import template

register = template.Library()

@register.simple_tag()
def multiply(hours, rate):
    # you would need to do any localization of the result here
    return hours * rate