# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-10 15:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inputdistri', '0078_inputprocurementtransactionlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteProcurementLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(max_length=30, unique=True)),
                ('produce_net_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_to_wallet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delete_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]