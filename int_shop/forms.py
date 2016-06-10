# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.template.context_processors import request

from int_shop.models import Category, Product, CartItem, User


class CreateCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = []


class CategoryUpdateForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = []


class CategoryDeleteForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = []


class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = []


class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = []


class ProductDeleteForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = []


class AddToCartForm(forms.ModelForm):

    class Meta:
        model = CartItem
        exclude = ['item', 'number']


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=64, required=True, min_length=2)
    last_name = forms.CharField(label='Фамилия', max_length=64, required=True, min_length=2)
    email = forms.EmailField(label='E-mail', max_length=64, required=True)
    password = forms.CharField(label='Пароль', max_length=64, required=True, min_length=5)
    confirm_password = forms.CharField(label='Подтверждение пароля', max_length=64, required=True, min_length=5)

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if not email:
            raise forms.ValidationError('Поле не должно быть пустым')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password', '')
        confirm_password = self.cleaned_data.get('confirm_password', '')

        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')

        return confirm_password


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=128, required=True)
    password = forms.CharField(label='password', max_length=128, required=True)
