# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-21 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0029_sowing_reason'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sowing',
            old_name='reason',
            new_name='reason_for_inactive',
        ),
    ]
