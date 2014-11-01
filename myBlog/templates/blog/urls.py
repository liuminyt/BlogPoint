from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'^topics/$', views.topics, name="topics"),
	url(r'^topics/(?P<topics_id>\d+)/$', views.topicsArticles, name="topicsArticles"),
	url(r'^(?P<articles_id>\d+)/$', views.article, name="article"),
	url(r'^likest/$', views.likest, name="likest"),
	url(r'^likeit/(?P<article_id>\d+)/$', views.likeit, name="likeit"),
	url(r'^labelArticles/(?P<articles_label>\w+)/$', views.labelArticles, name="labelArticles")
)
