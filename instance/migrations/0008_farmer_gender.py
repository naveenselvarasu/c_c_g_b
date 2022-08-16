# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-19 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0001_initial'),
        ('instance', '0007_auto_20200319_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='knowledgebase.Gender'),
            preserve_default=False,
        ),
    ]