import random

from int_shop.forms import LoginForm
from int_shop.models import Product


def login_form(request):
    return {'login_form': LoginForm}


def popular(request):
    obj_number = len(Product.objects.all())
    random3 = set()
    if obj_number >= 9:
        while len(random3) < 3:
            random3.add(random.choice(Product.objects.order_by('-count')[:9]))
    elif obj_number >= 3:
        while len(random3) < 3:
            random3.add(random.choice(Product.objects.order_by('-count')[:obj_number]))
    else:
        random3 = Product.objects.all()

    return {'popular': random3}
