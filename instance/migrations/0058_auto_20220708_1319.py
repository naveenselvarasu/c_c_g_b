# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-08 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0057_farmer_is_demo_farmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasonbasesfarmergpaquestionanswerlog',
            name='farmer_gap_log',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instance.SeasonBasesFarmerGpaLog'),
        ),
    ]
