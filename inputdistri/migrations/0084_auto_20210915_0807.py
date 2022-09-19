# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-09-15 08:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import inputdistri.models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0045_farmerbankdetails_remarks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inputdistri', '0083_auto_20210802_0549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=7, max_digits=10)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllowanceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelAllowanceDetilas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_kilometre', models.DecimalField(decimal_places=7, max_digits=10)),
                ('to_kilometre', models.DecimalField(decimal_places=7, max_digits=10)),
                ('from_captured_image', models.FileField(blank=True, max_length=1000, null=True, upload_to=inputdistri.models.upload_from_kilometre)),
                ('to_captured_image', models.FileField(blank=True, max_length=1000, null=True, upload_to=inputdistri.models.upload_to_kilometre)),
                ('allowance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Allowance')),
            ],
        ),
        migrations.CreateModel(
            name='UsertypewiseAllowanceCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=7, max_digits=10)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('allowance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.AllowanceType')),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.UserType')),
            ],
        ),
        migrations.AddField(
            model_name='allowance',
            name='allowance_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.AllowanceType'),
        ),
        migrations.AddField(
            model_name='allowance',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowance_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='allowance',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Season'),
        ),
        migrations.AddField(
            model_name='allowance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowance_created_for', to=settings.AUTH_USER_MODEL),
        ),
    ]
