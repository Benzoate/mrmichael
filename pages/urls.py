from django.conf.urls import patterns, include, url
from django.contrib import admin
from pages import views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'mrmichael.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index),
    url(r'^(?P<path>.*)/$', views.view_page),
)
