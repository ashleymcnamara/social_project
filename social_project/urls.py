from django.conf.urls import patterns, include, url
from apps.user.socialIntegration.apiCalls import *
from allaccess.views import *
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
	 url(r'^lists/', include('apps.lists.urls',namespace='lists')),
     url(r'^users/', include('apps.user.urls',namespace='user')),
    # Examples:
    # url(r'^$', 'social_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allaccess.urls')),
    url(r'^social_list/', include('social_list.urls')),
    url(r'^accounts/login$', 'django.contrib.auth.views.login'),

    #url(r'^accounts/', include('allaccess.urls')),
    url(r'^accounts/login/(?P<provider>(\w|-)+)/$', OAuthRedirect.as_view(), name='allaccess-login'),
    url(r'^accounts/callback/(?P<provider>(\w|-)+)/$', AdditionalUserInfoCallback.as_view(), name='allaccess-callback'),
   
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
