# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20170309_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]