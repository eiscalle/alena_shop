from django.conf.urls import url

from shop_api.views import ShopApiView

urlpatterns = [
    url(r'^api/v1/data$', ShopApiView.as_view(), name='shop_api'),
]
