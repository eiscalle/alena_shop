# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django import forms

from news.models import News


class CreateNewsForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = []


class NewsUpdateForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = []


class NewsDeleteForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = []
