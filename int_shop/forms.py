from django import forms

from int_shop.models import Category


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

