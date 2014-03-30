from django.conf.urls import patterns, include, url

from social_list import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.home, name='home'),

)
