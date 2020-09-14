from django import template
import re

regitser = tmeplate.Library()

@register.filter
def add_link(value):
    content = value.content
    tags = value.tag_set.all()
    for tag in tags:
        # content = re.sub(patterns, reql, conent)
        content = re.sub(r'\#' + tag.name + r'\b', '<a href="/post/explore/tags/' + tag.name '">#' + tag.name'</a>', content)
    return content