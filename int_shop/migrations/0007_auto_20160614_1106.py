# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('int_shop', '0006_auto_20160614_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pages',
            field=models.IntegerField(blank=True, default=None, verbose_name='Number of pages'),
        ),
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.DateField(blank=True, default=None, verbose_name='Publish date'),
        ),
    ]
