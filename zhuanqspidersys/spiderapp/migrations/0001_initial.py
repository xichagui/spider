# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('head_url', models.CharField(max_length=200, null=True)),
                ('fans', models.BigIntegerField(null=True)),
                ('popular', models.BigIntegerField(null=True)),
                ('sign', models.CharField(max_length=100, null=True)),
                ('kugou_url', models.URLField(blank=True, null=True)),
                ('kugou_is_vip', models.BooleanField(default=False)),
                ('kugou_is_realname', models.BooleanField(default=False)),
                ('kugou_is_tao', models.BooleanField(default=False)),
                ('kugou_is_musician', models.BooleanField(default=False)),
                ('kugou_is_liver', models.BooleanField(default=False)),
                ('kugou_is_recommend', models.BooleanField(default=False)),
                ('kugou_is_star', models.BooleanField(default=False)),
                ('kugou_is_mobile', models.BooleanField(default=False)),
                ('kugou_is_xinlang', models.BooleanField(default=False)),
                ('kugou_is_renren', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('type', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('upload_time', models.DateTimeField()),
                ('lrc', models.TextField(blank=True, max_length=500, null=True)),
                ('inspiration', models.TextField(blank=True, max_length=1000, null=True)),
                ('popular', models.BigIntegerField(blank=True, null=True)),
                ('click', models.BigIntegerField(blank=True, null=True)),
                ('download_count', models.BigIntegerField(blank=True, null=True)),
                ('collect', models.BigIntegerField(blank=True, null=True)),
                ('like', models.BigIntegerField(blank=True, null=True)),
                ('kugou_url', models.URLField(blank=True, null=True)),
                ('arrange', models.ManyToManyField(blank=True, related_name='arrange', to='spiderapp.Author')),
                ('composer', models.ManyToManyField(blank=True, related_name='composer', to='spiderapp.Author')),
                ('lyricist', models.ManyToManyField(blank=True, related_name='lyricist', to='spiderapp.Author')),
                ('mixer', models.ManyToManyField(blank=True, related_name='mixer', to='spiderapp.Author')),
                ('original_singer', models.ManyToManyField(blank=True, related_name='original_singer', to='spiderapp.Author')),
                ('singer', models.ManyToManyField(blank=True, related_name='singer', to='spiderapp.Author')),
                ('style', models.ManyToManyField(to='spiderapp.Style')),
            ],
        ),
    ]
