from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
#from store.views import ShopView

from store import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name='index'),
    url(r'^shop/', views.shop, name='shop'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^privacy/', views.privacy, name='privacy'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^shop_detail/(\w\d+)/$', views.shop_detail, name='shop_detail'),
    #url(r'^shop/$', ShopView.as_view(), name='shop'),
    #url(r'^shop/(?P<slug>[\w-]+)/$', views.shop_detail, name='shop_detail'),
)

urlpatterns += staticfiles_urlpatterns()
