from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from int_shop.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        response = super(ProductListView, self).get(request, *args, **kwargs)
        return response

     def get_queryset(self):


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


