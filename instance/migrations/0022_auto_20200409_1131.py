# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0021_auto_20200408_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerbankdetails',
            name='is_primary',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userbankdetails',
            name='is_primary',
            field=models.BooleanField(default=True),
        ),
    ]
