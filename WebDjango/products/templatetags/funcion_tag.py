from django import template

register = template.Library()


@register.filter
def precio_tag(value):
    if value is None or value == "":
        return "$0.00"

    try:
        val_numerico = float(value)
        return f"${val_numerico:,.2f}"
    except (ValueError, TypeError):
        return value
