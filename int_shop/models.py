# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    author = models.CharField(max_length=100, verbose_name=_('Author'), blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0, validators=[MinValueValidator(0)], null=False,
                                verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    category = models.ManyToManyField('Category', related_name='products', verbose_name=_('Category'), blank=True)
    is_hidden = models.BooleanField(_('Is hidden'), default=False)
    # image = models.ImageField(verbose_name=(_('Image')), null=True, default=None)
    pages = models.IntegerField(verbose_name=_('Number of pages'), blank=True, default=None, null=True)
    cover = models.CharField(max_length=50, verbose_name=_('Cover'), blank=True)
    publisher = models.CharField(max_length=50, verbose_name=_('Publisher'), blank=True)
    year = models.DateField(verbose_name=_('Publish date'), blank=True, default=None, null=True)
    sales_count = models.IntegerField(default=0, verbose_name=_('Sold'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))
    votes_count = models.IntegerField(default=0, verbose_name=_('Voted'))
    in_stock = models.IntegerField(default=0, verbose_name=_('In stock'))
    count = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    is_hidden = models.BooleanField(_('Is hidden'), default=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', verbose_name=_('Parent category'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.pk])

    def __unicode__(self):
        return self.title


class MainMenu(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('Title'))
    url = models.URLField(verbose_name=_('URL'))
    is_active = models.BooleanField(verbose_name=_('Is active'))
    order = models.IntegerField(default=0, verbose_name=_('Ordering'))

    class Meta:
        verbose_name = _('Main Menu')
        verbose_name_plural = _('Main Menues')


class Notification(models.Model):
    system_name = models.CharField(max_length=255, verbose_name=_('Slug'))
    subject = models.CharField(max_length=255, verbose_name=_('Subject'))
    template = models.CharField(max_length=255, verbose_name=_('Template'))
    email_template = models.TextField(verbose_name=_('Email Template'))
    sender = models.EmailField(verbose_name=_('Sender'))

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')


class User(AbstractUser):
    def __unicode__(self):
        return self.first_name


class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'))
    avatar = models.ImageField(null=True, default=None, verbose_name=_('Image'))
    birth_date = models.DateField(default=None, verbose_name=_('Date of Birth'))
    city = models.CharField(max_length=255, default=None, verbose_name=_('City'))
    country = models.CharField(max_length=255, default=None, verbose_name=_('Country'))
    address = models.TextField(default=None, verbose_name=_('Address'))

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class WishList(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('Product'), default=None)
    user = models.ForeignKey(User, verbose_name=_('User'))


class Comment(models.Model):
    text = models.TextField(verbose_name=_('Text'))
    sender = models.ForeignKey(User, verbose_name=_('User'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Sent'))


class CartItem(models.Model):
    item = models.ForeignKey(Product, verbose_name=_('Product'))
    number = models.IntegerField(default=0, verbose_name=_('Quantity'))

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.item.pk])

    def __unicode__(self):
        return self.item


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, related_name='carts', null=True, default=None, verbose_name=_('Product'))
    user = models.OneToOneField('User', related_name='cart', verbose_name=_('User'), default=None, null=True)

    @property
    def count_price(self):
        count = 0
        for item in self.items.all():
            count += item.item.price * item.number
        return count

    def get_absolute_url(self):
        return reverse('cart')


class Order(models.Model):
    CASH = 'CASH'
    CARD = 'CARD'
    PAYMENT_TYPE_CHOICES = (
        (CASH, _('Cash')),
        (CARD, _('Card')),
    )

    CREATED = _('Created')
    SENT = _('Sent')
    DELIVERED = _('Delivered')
    STATUS_CHOICES = (
        (CREATED, _('Created')),
        (SENT, _('Sent')),
        (DELIVERED, _('Delivered'))
    )

    items = models.ManyToManyField('OrderItem', related_name='orders', verbose_name=_('Items'))
    phone = models.CharField(max_length=255, default='', verbose_name=_('Phone'))
    address = models.CharField(max_length=150, verbose_name=_('Address'))
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES, default=CASH,
                                    verbose_name=_('Payment type'))
    user = models.ForeignKey(User, verbose_name=_('User'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=CREATED, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    @property
    def count_price(self):
        count = 0
        for item in self.items.all():
            count += item.item.price * item.number
        return count

    def get_absolute_url(self):
        return reverse('create_order')


class OrderItem(models.Model):
    item = models.ForeignKey(Product, verbose_name=_('Product'))
    number = models.IntegerField(default=0, verbose_name=_('Quantity'))
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0, validators=[MinValueValidator(0)], null=False,
                                verbose_name=_('Price'))

    def __unicode__(self):
        return self.item


class ProductProperty(models.Model):
    title = models.CharField(blank=False, default='', max_length=128, verbose_name='Property Title')
    product = models.ForeignKey(Product, blank=False, related_name='properties', verbose_name='Product')

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Property')

    def __unicode__(self):
        return self.product.title + ' : ' + self.title


class ProductPropertyValue(models.Model):
    property = models.ForeignKey(ProductProperty, blank=False, related_name='values', verbose_name='Property Title')
    title = models.CharField(blank=False, default='', max_length=128, verbose_name='Property Value')

    class Meta:
        verbose_name = _('Property Value')
        verbose_name_plural = _('Property Values')

    def __unicode__(self):
        return u'%s: %s:' % (self.property.product.title, self.title)

