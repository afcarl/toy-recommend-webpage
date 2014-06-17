from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from webapp.views.page_a import helloworld

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^helloworld/$', helloworld)
)
