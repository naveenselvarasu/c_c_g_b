# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-08-09 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inputdistri', '0111_auto_20220712_0652'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='allowance',
        #     name='date',
        #     field=models.DateField(default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
        migrations.AddField(
            model_name='procurement',
            name='utr_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        # migrations.AddField(
        #     model_name='travelallowancedetilas',
        #     name='date',
        #     field=models.DateField(default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
    ]