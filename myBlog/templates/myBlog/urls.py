from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from filebrowser.sites import site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls',namespace="blog")),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT,}),
)
