# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-27 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputdistri', '0023_procurement_other_deduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='procurement',
            name='remarks',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
