# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.contrib import admin
from django import forms
from blog.models import Articles, Comments, Topics, SiteConf

class ArticlesForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'vLargeTextField'}))
	class Meta:
		forms.model = Articles

class ArticlesAdmin(admin.ModelAdmin):
	list_display = ('headline', 'pub_date', 'like', 'topics')
	list_filter = ('pub_date','topics__name')
	form = ArticlesForm
	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/grappelli/tinymce_setup/tinymce_setup.js',
			'/static/google-code-prettify/prettify.js',
		]

# Register your models here.
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Comments)
admin.site.register(Topics)
admin.site.register(SiteConf)
