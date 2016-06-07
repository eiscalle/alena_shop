from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0, validators=[MinValueValidator(0)], verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'))
    category = models.ManyToManyField('Category', related_name='products', verbose_name=_('Category'))

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))