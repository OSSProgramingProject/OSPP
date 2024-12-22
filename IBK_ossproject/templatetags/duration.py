from django import template

register = template.Library()

@register.filter
def duration(value):
    hours, remainder = divmod(value, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{hours}시간 {minutes}분"
