# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-21 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='info2',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]