# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-20 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0009_auto_20200320_0432'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='afsclustermap',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='afsclustermap',
            name='assit_field_supervisor',
        ),
        migrations.RemoveField(
            model_name='afsclustermap',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='afsclustermap',
            name='field_supervisor',
        ),
        migrations.RemoveField(
            model_name='afsclustermap',
            name='season',
        ),
        migrations.DeleteModel(
            name='AfsClusterMap',
        ),
    ]
