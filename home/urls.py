from django.conf.urls import url
# from django.conf.urls import handler404, handler500

from . import views
# from home.views import e_handler404, e_handler500



# handler404 = 'home.views.e_handler404'
# handler500 = 'home.views.e_handler500'


urlpatterns = [
    url(r'^$', views.main, name='index'),
    url(r'^orders/$', views.orders, name='orders'),
    url(r'^complete/(?P<id>\d+)/$', views.orders, name='complete'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^confidential/$', views.confidential, name='confidential'),
    url(r'^oferta/$', views.oferta, name='oferta'),
    url(r'^telegram.me/milan_holidays_bot/$', views.telegram, name='telegram'),
    url(r'^instagram.com/milan_holidays/$', views.instagram, name='instagram'),

    url(r'^email/$', views.email, name='email'),
]
