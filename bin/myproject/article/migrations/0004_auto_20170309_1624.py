# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_article',
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_article',
            field=models.ManyToManyField(to='article.Article'),
        ),
    ]
