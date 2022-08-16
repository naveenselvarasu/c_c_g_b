# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-26 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0049_gapgradecv_seasonbasedgap_seasonbasesfarmergpalog_tempseasonbasedgap'),
        ('inputdistri', '0099_auto_20220522_1522'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='allowance',
        #     name='date',
        #     field=models.DateField(default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
        migrations.AddField(
            model_name='procurementfileupload',
            name='season',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='instance.Season'),
            preserve_default=False,
        ),
        # migrations.AddField(
        #     model_name='travelallowancedetilas',
        #     name='date',
        #     field=models.DateField(default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
    ]