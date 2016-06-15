# -*- coding: utf-8 -*-
import random

from django import template
from django.template.loader import render_to_string

from int_shop.models import Product

register = template.Library()


@register.inclusion_tag('popular.html', takes_context=False)
def popular(category=None):
    random3 = set()
    qs = Product.objects.order_by('-count')
    if category is not None:
        qs = qs.filter(category=category)
    if qs.count() < 3:
        random3 = qs
    else:
        while len(random3) < 3:
            random3.add(random.choice(qs[:9]))

    return {'popular': random3}
