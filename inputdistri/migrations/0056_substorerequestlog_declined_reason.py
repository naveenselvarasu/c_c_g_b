# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-06 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputdistri', '0055_auto_20210306_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='substorerequestlog',
            name='declined_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]