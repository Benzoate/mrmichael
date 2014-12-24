from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'pages.views.index'),
    url(r'^page/', include('pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
