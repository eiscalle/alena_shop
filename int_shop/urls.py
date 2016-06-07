from django.conf.urls import url

from int_shop.views import product_list_view, product_detail_view

urlpatterns = [
    url(r'^list/$', product_list_view, name='product_list'),
    url(r'^detail/(?P<pk>\d+)/$', product_detail_view, name='product_detail'),
]
