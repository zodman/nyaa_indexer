# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0005_auto_20160510_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='malmeta',
            old_name='synoms',
            new_name='resumen',
        ),
        migrations.AddField(
            model_name='malmeta',
            name='synopsys',
            field=models.TextField(blank=True, null=True),
        ),
    ]
