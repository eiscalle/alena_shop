from django import forms

from int_shop.models import Category, Product, CartItem


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
