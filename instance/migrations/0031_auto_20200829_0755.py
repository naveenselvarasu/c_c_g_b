# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-29 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0030_auto_20200821_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='sowing',
            name='geo_fence_done_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sowing',
            name='is_geo_fencing_is_automatic',
            field=models.BooleanField(default=False),
        ),
    ]
