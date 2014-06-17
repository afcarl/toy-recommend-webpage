from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from webapp.views.pages import view_page_a, view_page_b, view_page_c, clear_cache

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^page-a/$', view_page_a),
    url(r'^page-b/$', view_page_b),
    url(r'^page-c/$', view_page_c),
    url(r'^clear-cache/$', clear_cache),
)
