# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osmdata', '0005_osmelement_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minlat', models.FloatField()),
                ('minlon', models.FloatField()),
                ('maxlat', models.FloatField()),
                ('maxlon', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='osmelement',
            name='bounds',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='osmdata.Bounds'),
        ),
    ]
