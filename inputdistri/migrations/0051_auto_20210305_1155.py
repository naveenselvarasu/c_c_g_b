# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-05 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputdistri', '0050_auto_20210305_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='substorerequestlog',
            name='section',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='substorerequestlog',
            name='sub_section',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]