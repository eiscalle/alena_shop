# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.db.models import F
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from int_shop.forms import CreateCategoryForm, CategoryUpdateForm, CreateProductForm, ProductUpdateForm, AddToCartForm, \
    RegistrationForm, LoginForm, OrderDetailForm, OrderCreateForm
from int_shop.models import Product, Category, Cart, CartItem, User, Order


class RootView(TemplateView):
    template_name = 'base.html'


root_view = RootView.as_view()


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        return qs.filter(is_hidden=False)


product_list_view = ProductListView.as_view()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_object(self, queryset=None):
        obj = super(ProductDetailView, self).get_object(queryset)
        obj.count += 1
        obj.save()
        return obj


product_detail_view = ProductDetailView.as_view()


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = CreateProductForm

    def get_success_url(self):
        return reverse('product_list')


product_create_view = ProductCreateView.as_view()


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductUpdateForm

    def get_success_url(self):
        return reverse('product_list')


product_update_view = ProductUpdateView.as_view()


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'

    def get_success_url(self):
        return reverse('product_list')


product_delete_view = ProductDeleteView.as_view()


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

    def get_queryset(self):
        qs = super(CategoryListView, self).get_queryset()
        return qs.filter(is_hidden=False)


category_list_view = CategoryListView.as_view()


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['products'] = self.object.products.filter(is_hidden=False)
        return context


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


class CartView(DetailView):
    model = Cart
    template_name = 'cart.html'

    def get_object(self, queryset=None):
        return self.model.objects.get_or_create(user=self.request.user)[0]

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['cart_items'] = self.object.items.all()
        context['total_price'] = self.object.count_price
        return context


cart_view = CartView.as_view()


class AddToCartView(CreateView):
    model = CartItem
    template_name = 'cart_item.html'
    form_class = AddToCartForm

    def form_valid(self, form):
        form.instance.item = Product.objects.get(pk=self.kwargs['pk'])
        form.instance.number = 1
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        if cart.items.filter(item__pk=self.kwargs['pk']).exists():
            cart.items.filter(item__pk=self.kwargs['pk']).update(number=F('number') + 1)
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = form.save()
            cart.items.add(self.object)
        return super(AddToCartView, self).form_valid(form)

    def get_success_url(self):
        return reverse('cart')


add_to_cart_view = AddToCartView.as_view()


class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'cart_item_delete.html'

    def get_success_url(self):
        return reverse('cart')

cart_item_delete_view = CartItemDeleteView.as_view()


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success = False
    request = None

    def post(self, request, *args, **kwargs):
        self.request = request
        return super(RegistrationView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)

        context['success'] = self.success
        return context

    def form_valid(self, form):
        user = User.objects.create_user(username=form.cleaned_data['email'],
                                        email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name']
                                        )

        auth_user = authenticate(username=user.username, password=form.cleaned_data['password'])
        login(self.request, auth_user)

        redirect_to = self.request.META['HTTP_REFERER']

        subject = 'Hello %s' % user.username
        message = 'Welcome'
        user.email_user(subject, message)

        return HttpResponseRedirect(redirect_to)


registration_view = RegistrationView.as_view()


def login_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    remember_me = request.POST.get('remember_me', None)

    form = LoginForm(request.POST)

    request.session['LoginErrors'] = dict(form.errors)

    auth_user = authenticate(username=username, password=password)
    if auth_user:
        login(request, auth_user)

        if not remember_me:
            request.session.set_expiry(0)
    elif username != '' and password != '':
        request.session['LoginErrors']['username'] = ['Ошибка входа',]

    if request.GET.get('next', ''):
        redirect_to = request.GET.get('next', '')
    else:
        redirect_to = request.META.get('HTTP_REFERER', '')

    redirect_to = redirect_to if redirect_to else '/'

    return HttpResponseRedirect(redirect_to)


def logout_user(request):
    logout(request)
    redirect_to = '/'
    return HttpResponseRedirect(redirect_to)


class PopularListView(ListView):
    model = Product
    template_name = 'popular_list.html'

    def get_queryset(self):
        qs = super(PopularListView, self).get_queryset()
        return qs.filter(is_hidden=False)


popular_list_view = PopularListView.as_view()


class OrderDetailView(CreateView):
    model = Order
    template_name = 'order_detail.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(user=self.request.user)[0]

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['order_items'] = self.object.items.all()
        context['total_price'] = self.object.count_price
        return context


order_detail_view = OrderDetailView.as_view()


class OrderCreateView(CreateView):
    model = Order
    template_name = 'create_order.html'
    form_class = OrderCreateForm

order_create_view = OrderCreateView.as_view()


class SendOrderView(TemplateView):
    template_name = 'send_order.html'


send_order_view = SendOrderView.as_view()









