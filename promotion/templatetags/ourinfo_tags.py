from django import template
from promotion.models import OurInformation

register = template.Library()

@register.simple_tag
def get_ourinfo():
    return OurInformation.objects.all()
