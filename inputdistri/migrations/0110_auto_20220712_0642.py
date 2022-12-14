# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-12 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inputdistri', '0109_auto_20220708_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paymentstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        # migrations.AddField(
        #     model_name='allowance',
        #     name='date',
        #     field=models.DateField(default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
        migrations.AddField(
            model_name='procurement',
            name='reason_for_payment_hold',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        # migrations.AddField(
        #     model_name='travelallowancedetilas',
        #     name='date',
        #     field=models.DateField(default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
    ]
