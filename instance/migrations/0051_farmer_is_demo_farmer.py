# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-22 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0050_auto_20220622_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='is_demo_farmer',
            field=models.BooleanField(default=False),
        ),
    ]
