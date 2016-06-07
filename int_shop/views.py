from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render_to_response
from int_shop.forms import CreateCategoryForm, CategoryUpdateForm

from int_shop.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        response = super(ProductListView, self).get(request, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['bla'] = 'nebla'
        return context


product_list_view = ProductListView.as_view()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    http_method_names = ['GET']

    def get_object(self, queryset=None):
        super(ProductDetailView, self).get_object()

product_detail_view = ProductDetailView.as_view()


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


category_list_view = CategoryListView.as_view()


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'


category_detail_view = CategoryDetailView.as_view()


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_create.html'
    form_class = CreateCategoryForm

    def get_success_url(self):
        return reverse('category_list')


category_create_view = CategoryCreateView.as_view()


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_update.html'
    form_class = CategoryUpdateForm

    def get_success_url(self):
        return reverse('category_list')


category_update_view = CategoryUpdateView.as_view()


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'

    def get_success_url(self):
        return reverse('category_list')

category_delete_view = CategoryDeleteView.as_view()
