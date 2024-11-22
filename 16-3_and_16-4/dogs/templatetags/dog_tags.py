from django import template

register = template.Library()

@register.filter
def uppercase(value):
    """Преобразует строку в верхний регистр."""
    return value.upper()
