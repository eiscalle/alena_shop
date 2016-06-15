import random

from int_shop.forms import LoginForm
from int_shop.models import Product, Category


def login_form(request):
    return {'login_form': LoginForm}


# def popular(request):
#     random3 = set()
#     while len(random3) < 3:
#         random3.add(random.choice(Product.objects.order_by('-count')[:9]))
#     return {'popular': random3}
