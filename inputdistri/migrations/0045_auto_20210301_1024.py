# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-01 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputdistri', '0044_auto_20210301_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentinventory',
            name='label_range_from',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='agentinventory',
            name='label_range_to',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
