# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='upload_time',
            field=models.DateTimeField(null=True),
        ),
    ]