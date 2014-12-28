from django.conf.urls import patterns, include, url
from django.contrib import admin
from pictures import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index),
    url(r'^image/(?P<pk>\d+)/$', views.get_image),
    url(r'^thumb/(?P<pk>\d+)/$', views.get_thumbnail),
    url(r'^album/(?P<album_id>\d+|new)/$', views.album)
)
