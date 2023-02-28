from django import template
from student.models import Category


register = template.Library()


@register.simple_tag(name='categories')
def get_categories():
    return Category.objects.all()
