from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls')),
    url(r'^accounts/', include('authentication.urls')),
    url(r'^password_reset/', include('password_reset.urls')),
    url(r'^tshirt-contest/', include('tshirt_contest.urls')),
  ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)