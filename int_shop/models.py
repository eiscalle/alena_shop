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
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0, validators=[MinValueValidator(0)],
                                verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    category = models.ManyToManyField('Category', related_name='products', verbose_name=_('Category'), blank=True)
    is_hidden = models.BooleanField(_('Is hidden'), default=False)
    image = models.ImageField(verbose_name=(_('Image')), null=True, default=None)
    pages = models.IntegerField(verbose_name=_('Number of pages'), blank=True, default=None, null=True)
    cover = models.CharField(max_length=50, verbose_name=_('Cover'), blank=True)
    publisher = models.CharField(max_length=50, verbose_name=_('Publisher'), blank=True)
    year = models.DateField(verbose_name=_('Publish date'), blank=True, default=None, null=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    is_hidden = models.BooleanField(_('Is hidden'), default=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.pk])

    def __unicode__(self):
        return self.title


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


class User(AbstractUser):
    def __unicode__(self):
        return self.first_name
