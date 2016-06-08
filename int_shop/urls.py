from django.conf.urls import url

from int_shop.views import product_list_view, product_detail_view, category_list_view, category_detail_view, \
    category_create_view, category_update_view, category_delete_view, product_create_view, product_update_view, product_delete_view, root_view, \
    cart_view, add_to_cart_view, cart_item_delete_view

urlpatterns = [
    url(r'^product/list/$', product_list_view, name='product_list'),
    url(r'^$', root_view, name='root'),
    url(r'^category/list/$', category_list_view, name='category_list'),
    url(r'^category/detail/(?P<pk>\d+)/$', category_detail_view, name='category_detail'),
    url(r'^category/create/$', category_create_view, name='create_category'),
    url(r'^category/update/(?P<pk>\d+)/$', category_update_view, name='update_category'),
    url(r'^category/delete(?P<pk>\d+)/$', category_delete_view, name='delete_category'),
    url(r'^product/detail/(?P<pk>\d+)/$', product_detail_view, name='product_detail'),
    url(r'^product/create/$', product_create_view, name='create_product'),
    url(r'^product/update/(?P<pk>\d+)/$', product_update_view, name='update_product'),
    url(r'^product/delete/(?P<pk>\d+)/$', product_delete_view, name='delete_product'),
    url(r'^cart/$', cart_view, name='cart'),
    url(r'^product/addtocart/(?P<pk>\d+)/$', add_to_cart_view, name='add_to_cart'),
    url(r'^cart/delete(?P<pk>\d+)/$', cart_item_delete_view, name='delete_item_from_cart'),


]
