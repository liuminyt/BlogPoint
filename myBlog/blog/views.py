# _*_ coding:UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render,get_object_or_404
from blog.models import SiteConf, Articles,Comments, Topics
from django.http import HttpResponse
# Create your views here.

def index(request):
	siteinfo = SiteConf.objects.get(pk=1)
	articles = Articles.objects.all().order_by('-id')
	comments = Comments.objects.all()
	return render(request, 'blog/index.html', {'siteinfo': siteinfo,'articles': articles})

def likest(request):
	siteinfo = SiteConf.objects.get(pk=1)
	articles = Articles.objects.all().order_by('-like')
	comments = Comments.objects.all()
	return render(request, 'blog/likest.html', {'siteinfo': siteinfo,'articles': articles})

def topics(request):
	siteinfo = SiteConf.objects.get(pk=1)
	topics = Topics.objects.all()
	return render(request, 'blog/topicslist.html', {'siteinfo': siteinfo,'topics': topics })

def topicsArticles(request, topics_id):
	siteinfo = SiteConf.objects.get(pk=1)
	topic = get_object_or_404(Topics, pk=topics_id)
	articles = Articles.objects.filter(topics = topics_id)
	return render(request, 'blog/topicsArticles.html', {'siteinfo': siteinfo, 'topic': topic, 'articles': articles })

def article(request, articles_id):
	siteinfo = SiteConf.objects.get(pk=1)
	article = Articles.objects.get(pk = articles_id)
	return render(request, 'blog/article.html', {'siteinfo': siteinfo, 'article': article })

def labelArticles(request, articles_label):
	siteinfo = SiteConf.objects.get(pk=1)
	articles = Articles.objects.filter(label = articles_label)
	return render(request, 'blog/labelArticles.html', {'siteinfo': siteinfo, 'articles': articles, 'label': articles_label })

def likeit(request, article_id):
	likecount = 0;
	article = Articles.objects.get(id=article_id)
	likecount = article.like + 1
	article.like = likecount
	article.save()
	return HttpResponse(likecount)
	
