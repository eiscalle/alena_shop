from copy import deepcopy

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from int_shop.models import Product
from news.models import News
from shop_api.serializers import ProductSerializer, NewsSerializer


class ShopApiView(GenericAPIView):

    def get(self, request, **kwargs):

        serializer = ProductSerializer
        qs = Product.objects.all()
        product_data = serializer(qs, many=True).data

        serializer = NewsSerializer
        qs = News.objects.all()
        news_data = serializer(qs, many=True).data

        return Response({'product_data': product_data,
                         'news_data': news_data})


