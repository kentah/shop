from django.conf.urls import patterns, url

from store import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^shop/', views.shop, name='shop'),
    url(r'^join/', views.join, name='join'),
    url(r'^sign-in/', views.sign_in, name='sign_in'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^privacy/', views.privacy, name='privacy'),
)
