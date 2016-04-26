# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0002_auto_20160426_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malmeta',
            name='alternative_title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='malmeta',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='malmeta',
            name='synoms',
            field=models.TextField(blank=True, null=True),
        ),
    ]
