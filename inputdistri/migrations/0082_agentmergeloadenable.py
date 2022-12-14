# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-02 05:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0045_farmerbankdetails_remarks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inputdistri', '0081_inputdistributionotherstoretransactionmap'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentMergeloadEnable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Enabled_by', to=settings.AUTH_USER_MODEL)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Season')),
            ],
        ),
    ]
