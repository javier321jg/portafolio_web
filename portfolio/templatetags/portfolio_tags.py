from django import template

register = template.Library()


@register.filter
def split_tech(value):
    """
    Divide una cadena de tecnologías separadas por coma y limpia espacios.
    Uso: {{ project.technologies|split_tech }}
    """
    if not value:
        return []
    return [tech.strip() for tech in value.split(',')]
