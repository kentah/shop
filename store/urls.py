from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
#from store.views import ShopView

from store import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name='index'),
    #url(r'^about/', views.about, name='about'),
    #url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^shop/', views.shop, name='shop'),
    url(r'^join/', views.join, name='join'),
    url(r'^sign-in/', views.sign_in, name='sign_in'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^privacy/', views.privacy, name='privacy'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^shop_detail/', views.shop_detail, name='shop_detail'),
    #url(r'^shop_detail(?P<pk>\d+)/$', ShopView.as_view(), name='shop_detail'),
    #url(r'^shop/(?P<slug>[\w-]+)/$', views.shop_detail, name='shop_detail'),
    #url(r'^/join_form/$', views.join, name="join_form"),
)

urlpatterns += staticfiles_urlpatterns()
