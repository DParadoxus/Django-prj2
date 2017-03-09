# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20170309_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_article',
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
            preserve_default=False,
        ),
    ]
