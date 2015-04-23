from django.conf.urls import include, url, patterns

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'signup.views.home', name='home'),
    url(r'^about/$', 'signup.views.about', name='about' ),
    url(r'^thank/$','signup.views.thank', name='thank' ),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)