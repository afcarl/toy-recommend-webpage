from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from webapp.views.pages import page_a, page_b, page_c

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^page-a/$', page_a),
    url(r'^page-b/$', page_b),
    url(r'^page-c/$', page_c),
)
