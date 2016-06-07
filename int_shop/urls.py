from django.conf.urls import url

from int_shop.views import product_list_view, product_detail_view, category_list_view, category_detail_view, \
    category_create_view, category_update_view, category_delete_view

urlpatterns = [
    url(r'^list/$', product_list_view, name='product_list'),
    url(r'^detail/(?P<pk>\d+)/$', product_detail_view, name='product_detail'),
    url(r'^$', category_list_view, name='category_list'),
    url(r'^categories/$', category_list_view, name='category_list'),
    url(r'^detailed-category/(?P<pk>\d+)/$', category_detail_view, name='category_detail'),
    url(r'^createcategory/$', category_create_view, name='create_category'),
    url(r'^updatecategory/(?P<pk>\d+)/$', category_update_view, name='update_category'),
    url(r'^deletecategory/(?P<pk>\d+)/$', category_delete_view, name='delete_category'),
]
