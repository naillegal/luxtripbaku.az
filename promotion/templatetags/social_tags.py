from django import template
from promotion.models import Social

register = template.Library()

@register.simple_tag
def get_social():
    return Social.objects.all()
