# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-06 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0025_auto_20200525_0823'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='idbank',
            unique_together=set([]),
        ),
    ]