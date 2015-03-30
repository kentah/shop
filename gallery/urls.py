from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^store/', include('store.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'*/store/static/store_images/', include('store.urls')),
    #url(r'^templates/store/', include('store.urls')),  #works!

)


urlpatterns += staticfiles_urlpatterns()