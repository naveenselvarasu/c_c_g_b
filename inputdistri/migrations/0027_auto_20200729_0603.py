# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-29 06:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0028_auto_20200708_0633'),
        ('inputdistri', '0026_auto_20200728_1341'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='harvest',
            unique_together=set([('sowing', 'date_of_harvest', 'value', 'ticket_number')]),
        ),
    ]
