from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^store/', include('store.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'*/store/static/store_images/', include('store.urls')),
    #url(r'^templates/store/', include('store.urls')),  #works!

) 

#urlpatterns += staticfiles_urlpatterns()


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)