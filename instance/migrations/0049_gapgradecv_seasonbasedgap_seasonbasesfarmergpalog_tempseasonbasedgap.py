# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-16 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instance', '0048_userhierarchymap_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='GapGradeCv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('ordinal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SeasonBasedGap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=50)),
                ('followup_date', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('ordinal', models.IntegerField()),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasonbasedgap_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasonbasedgap_modified_by', to=settings.AUTH_USER_MODEL)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Season')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonBasesFarmerGpaLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tp_date', models.DateField()),
                ('expected_date', models.DateField()),
                ('actual_date', models.DateField()),
                ('variations', models.PositiveIntegerField(verbose_name='action_day_differences')),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasonbasesfarmergpalog_created_by', to=settings.AUTH_USER_MODEL)),
                ('gap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.SeasonBasedGap')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instance.GapGradeCv')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasonbasesfarmergpalog_modified_by', to=settings.AUTH_USER_MODEL)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Season')),
                ('sowing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Sowing')),
            ],
        ),
        migrations.CreateModel(
            name='TempSeasonBasedGap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=50)),
                ('followup_date', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('ordinal', models.IntegerField()),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tempseasonbasedgap_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tempseasonbasedgap_modified_by', to=settings.AUTH_USER_MODEL)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Season')),
            ],
        ),
    ]
