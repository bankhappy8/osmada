# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osmdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='members',
        ),
        migrations.AlterField(
            model_name='relationmember',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='osmdata.Relation'),
        ),
    ]
