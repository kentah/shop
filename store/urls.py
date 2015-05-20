from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

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
    #url(r'^/join_form/$', views.join, name="join_form"),
)

urlpatterns += staticfiles_urlpatterns()
