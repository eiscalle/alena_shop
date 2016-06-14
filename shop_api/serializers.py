from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from int_shop.models import Product
from news.models import News


class ProductSerializer(serializers.ModelSerializer):
    category = SerializerMethodField()

    def get_category(self, obj):
        return obj.category.values_list('title', flat=True)


    class Meta:
        model = Product
        fields = ('title', 'author', 'price', 'description', 'category', 'is_hidden', 'pages', 'cover', 'publisher',
                  'year', 'count')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'description')
