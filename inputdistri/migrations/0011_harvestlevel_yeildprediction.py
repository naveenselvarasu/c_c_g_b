# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-05 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0025_auto_20200525_0823'),
        ('inputdistri', '0010_auto_20200603_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='HarvestLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_name', models.CharField(max_length=50)),
                ('harvest_interval_duration_in_days', models.CharField(max_length=50)),
                ('notice_period', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='YeildPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acre', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('expected_yeild_weight_in_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Crop')),
                ('harvest_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.HarvestLevel')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Season')),
            ],
        ),
    ]
