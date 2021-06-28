from django.conf.urls import url
from . import views
from blog.views import BlogsListView, BlogDetailView


urlpatterns = [
url(r'^$', BlogsListView.as_view(), name='blog'), # то есть по URL http://имя_сайта/blog/
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', BlogDetailView.as_view()), # а по URL http://имя_сайта/blog/число/
                                              # будет выводиться пост с определенным номером
]
