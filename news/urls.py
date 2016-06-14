from django.conf.urls import url

from news.views import news_list_view, news_detail_view, news_create_view, news_update_view, news_delete_view

urlpatterns = [
    url(r'^news/list/$', news_list_view, name='news_list'),
    url(r'^news/detail/(?P<pk>\d+)/$', news_detail_view, name='news_detail'),
    url(r'^news/create/$', news_create_view, name='create_news'),
    url(r'^news/update/(?P<pk>\d+)/$', news_update_view, name='update_news'),
    url(r'^news/delete(?P<pk>\d+)/$', news_delete_view, name='delete_news'),
]
