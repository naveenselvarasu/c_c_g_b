# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-01 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inputdistri', '0077_inputdistributiontransactionmap_inputreturntransactionlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputProcurementTransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Procurement')),
                ('transaction_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.AgentTransactionLog')),
            ],
        ),
    ]
