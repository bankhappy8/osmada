# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmdata', '0002_auto_20161012_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='osmelement',
            name='version',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
