# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models

# Create your models here.
class Topics(models.Model):
	"""docstring for Topics"""
	name = models.CharField('专题名称', max_length=32)
	discreption = models.CharField('描述', max_length=200)
	image = models.ImageField('展示图片', upload_to='uploadImages')
	discreption_image = models.ImageField('专题图标', upload_to='uploadImages')
	def __unicode__(self):
		return '%s' %(self.name)
	class Meta:
		verbose_name_plural = '专题'
		
class Articles(models.Model):
	"""docstring for Atrcles"""
	headline = models.CharField('标题', max_length=200)
	content = models.CharField('内容信息',max_length=9600)
	pub_date = models.DateField('发布时间')
	image = models.ImageField('图片', upload_to="uploadImages")
	label = models.CharField('标签', max_length=32)
	like = models.IntegerField('喜欢', default=0)
	topics = models.ForeignKey(Topics,  verbose_name='所属专题')
	def __unicode__(self):
		return self.headline
	class Meta:
		verbose_name_plural = '文章'

class Comments(models.Model):
	"""docstring for Comments"""
	nickname = models.CharField('昵称', max_length=32)
	content = models.CharField('评论内容', max_length=2048)
	pub_date = models.DateField('评论时间')
	arictle = models.ForeignKey(Articles, verbose_name='被评论文章')
	def __unicode__(self):
		return '%s' %(self.nickname)
	class Meta:
		verbose_name_plural = '评论'


class SiteConf(models.Model):
	"""docstring for SiteConf"""
	username = models.CharField('用户名称', max_length=48)
	user_signature = models.CharField('个性签名', max_length=200)
	index_image = models.ImageField('首页展示图片', upload_to='uploadImages')
	user_image = models.ImageField('用户头像', upload_to='uploadImages')
	weichat_image = models.ImageField('微信二维码', upload_to='uploadImages')
	def __unicode__(self):
		return self.username
	class Meta:
		verbose_name_plural = '站点全局设置'
		



