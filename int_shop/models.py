# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0, validators=[MinValueValidator(0)],
                                verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'))
    category = models.ManyToManyField('Category', related_name='products', verbose_name=_('Category'))
    is_hidden = models.BooleanField(_('Is hidden'), default=False)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    is_hidden = models.BooleanField(_('Is hidden'), default=False)

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.pk])

    def __unicode__(self):
        return self.title


class CartItem(models.Model):
    item = models.ForeignKey(Product, verbose_name='Товар')
    number = models.IntegerField(default=0, verbose_name='Количество')

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.item.pk])

    def __unicode__(self):
        return self.item


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, related_name='carts', null=True, default=None, verbose_name='Товар')

    @property
    def count_price(self):
        count = 0
        for item in self.items.all():
            count += item.item.price * item.number
        return count

    def get_absolute_url(self):
        return reverse('cart')

