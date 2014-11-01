# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atrcles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.CharField(max_length=9600, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9\xe4\xbf\xa1\xe6\x81\xaf')),
                ('pub_date', models.DateField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('image', models.ImageField(upload_to=b'uploadImages', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('label', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
                ('like', models.IntegerField(default=0, verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2')),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=32, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('content', models.CharField(max_length=2048, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('pub_date', models.DateField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('arictle', models.ForeignKey(verbose_name=b'\xe8\xa2\xab\xe8\xaf\x84\xe8\xae\xba\xe6\x96\x87\xe7\xab\xa0', to='blog.Atrcles')),
            ],
            options={
                'verbose_name_plural': '\u8bc4\u8bba',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteConf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=48, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('user_signature', models.CharField(max_length=200, verbose_name=b'\xe4\xb8\xaa\xe6\x80\xa7\xe7\xad\xbe\xe5\x90\x8d')),
                ('index_image', models.ImageField(upload_to=b'uploadImages', verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\xb1\x95\xe7\xa4\xba\xe5\x9b\xbe\xe7\x89\x87')),
                ('user_image', models.ImageField(upload_to=b'uploadImages', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa4\xb4\xe5\x83\x8f')),
                ('weichat_image', models.ImageField(upload_to=b'uploadImages', verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1\xe4\xba\x8c\xe7\xbb\xb4\xe7\xa0\x81')),
            ],
            options={
                'verbose_name_plural': '\u7ad9\u70b9\u5168\u5c40\u8bbe\u7f6e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\x93\xe9\xa2\x98\xe5\x90\x8d\xe7\xa7\xb0')),
                ('discreption', models.CharField(max_length=200, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('image', models.ImageField(upload_to=b'uploadImages', verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe5\x9b\xbe\xe7\x89\x87')),
                ('discreption_image', models.ImageField(upload_to=b'uploadImages', verbose_name=b'\xe4\xb8\x93\xe9\xa2\x98\xe5\x9b\xbe\xe6\xa0\x87')),
            ],
            options={
                'verbose_name_plural': '\u4e13\u9898',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atrcles',
            name='topics',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\x93\xe9\xa2\x98', to='blog.Topics'),
            preserve_default=True,
        ),
    ]
