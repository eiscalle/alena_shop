# -*- coding: utf-8 -*-

from django.contrib.admin import ModelAdmin, register
from django.utils.translation import ugettext_lazy as _

from models import Product, Category, MainMenu, Notification, UserProfile, WishList, Order, ProductProperty, \
    ProductPropertyValue


@register(Product)
class ProductAdmin(ModelAdmin):

    def get_category(self, obj):
        category_list = obj.category.values_list('title', flat=True)
        return ', '.join(category_list)

    get_category.short_description = _('Category')

    list_display = ('title', 'author', 'price', 'in_stock', 'description', 'get_category', 'is_hidden', 'pages', 'cover', 'publisher', 'year', 'sales_count', 'rating', 'votes_count')


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('title', 'description', 'is_hidden', 'parent')


@register(MainMenu)
class MainMenuAdmin(ModelAdmin):
    list_display = ('title', 'url', 'is_active', 'order')


@register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display = ('system_name', 'subject', 'template', 'email_template', 'sender')


@register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'avatar', 'birth_date', 'city', 'country', 'address')


@register(Order)
class OrderAdmin(ModelAdmin):

    def get_items(self, obj):
        items = obj.items.values_list('item__title', flat=True)
        return ', '.join(items)

    get_items.short_description = _('Items')

    list_display = ('user', 'get_items', 'created_at', 'phone', 'address', 'payment_type', 'address', 'status')


@register(ProductProperty)
class ProductPropertyAdmin(ModelAdmin):
    list_display = ('product', )


@register(ProductPropertyValue)
class ProductPropertyValueAdmin(ModelAdmin):
    list_display = ('property', 'title')





