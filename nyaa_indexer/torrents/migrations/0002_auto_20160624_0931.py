# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-24 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]