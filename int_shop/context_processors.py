import random

from int_shop.forms import LoginForm
from int_shop.models import Product, Category


def login_form(request):
    return {'login_form': LoginForm}


def popular(request):
    obj_number = len(Product.objects.all())
    random3 = set()
    if obj_number >= 9:
        while len(random3) < 3:
            random3.add(random.choice(Product.objects.order_by('-count')[:9]))
    else:
        while len(random3) < 3:
            random3.add(random.choice(Product.objects.order_by('-count')[:obj_number]))

    return {'popular': random3}
