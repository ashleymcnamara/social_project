from django import template
from apps.lists.models import *
from apps.lists.forms import *

register = template.Library()

@register.inclusion_tag('../templates/components/ajax_modal.html')
def ajax_modal( ):
    return {

    }

