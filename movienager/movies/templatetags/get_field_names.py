from django import template
from django.db import models

register = template.Library()

@register.filter()
def get_field_names(obj):
    return [field.verbose_name for field in obj._meta.get_fields() if not(field.name == 'id' or isinstance(field, models.ManyToOneRel) or isinstance(field, models.ManyToManyRel))]
