from django import template

register = template.Library()

@register.filter()
def get_field_names(obj):
    return [field.verbose_name for field in obj._meta.get_fields() if field.name != 'id']
