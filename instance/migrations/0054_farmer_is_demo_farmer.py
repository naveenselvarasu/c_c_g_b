# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-26 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0053_auto_20220626_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='is_demo_farmer',
            field=models.BooleanField(default=False),
        ),
    ]
