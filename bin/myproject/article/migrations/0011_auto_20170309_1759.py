# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20170309_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_text',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
    ]
