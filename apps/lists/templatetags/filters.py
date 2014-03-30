from django import template
from apps.lists.models import *
from apps.lists.forms import *

register = template.Library()

@register.inclusion_tag('../templates/components/filter_menu.html')
def menu( request ):
    return {'request':request

    }

