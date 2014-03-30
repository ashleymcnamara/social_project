__author__ = 'ashley'
from django.conf.urls import patterns
from django.conf.urls import url
from apps.lists import views
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^$', views.list_, name='list'),
                       url(r'^LIST/(?P<LIST_id>\d+)$',  views.view, name='view'),
                       url(r'^LIST/edit(?P<LIST_id>\d+)$',  views.edit, name='edit'),
                       url(r'^LIST/complete(?P<LIST_id>\d+)$',  views.complete, name='complete'),
                       url(r'^LIST/delete(?P<LIST_id>\d+)$',  views.delete, name='delete'),
                       url(r'^LIST/add$',  views.add, name='add'),
                       url(r'^LIST/random$',  views.random, name='random'),
                       url(r'^filters$',  views.filters, name='filters'),
                       )

