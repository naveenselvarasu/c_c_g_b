# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-02-26 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0047_usertype_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhierarchymap',
            name='season',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instance.Season'),
            preserve_default=False,
        ),
    ]