# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from news.forms import CreateNewsForm, NewsUpdateForm
from news.models import News


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'

    def get_queryset(self):
        qs = super(NewsListView, self).get_queryset()
        return qs


news_list_view = NewsListView.as_view()


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['news'] = self.object.all()
        return context


news_detail_view = NewsDetailView.as_view()


class NewsCreateView(CreateView):
    model = News
    template_name = 'news_create.html'
    form_class = CreateNewsForm

    def get_success_url(self):
        return reverse('category_list')


news_create_view = NewsCreateView.as_view()


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news_update.html'
    form_class = NewsUpdateForm

    def get_success_url(self):
        return reverse('news_list')


news_update_view = NewsUpdateView.as_view()


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news_delete.html'

    def get_success_url(self):
        return reverse('news_list')

news_delete_view = NewsDeleteView.as_view()