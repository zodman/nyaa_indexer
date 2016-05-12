# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0011_releasegroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metatorrent',
            name='fansub',
        ),
        migrations.AddField(
            model_name='fansub',
            name='release_groups',
            field=models.ManyToManyField(to='torrents.ReleaseGroup'),
        ),
        migrations.AddField(
            model_name='metatorrent',
            name='release_group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='torrents.ReleaseGroup'),
            preserve_default=False,
        ),
    ]
