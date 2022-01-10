from django import template
from mainapp.models import Product, Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()
