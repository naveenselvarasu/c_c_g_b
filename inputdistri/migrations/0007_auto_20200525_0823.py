# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-25 08:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instance', '0025_auto_20200525_0823'),
        ('inputdistri', '0006_inputitemreturnlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentTransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(blank=True, max_length=20, null=True)),
                ('wallet_balance_before_this_transaction', models.DecimalField(decimal_places=2, max_digits=10)),
                ('wallet_balance_after_this_transaction', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AgentWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('credit_limit', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('agent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_wallet_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InputDistributionTransactionMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InputReturnTransactionMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_item_return', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputItemReturnLog')),
                ('transaction_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.AgentTransactionLog')),
            ],
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty_vehicle_timestamp', models.DateTimeField()),
                ('empty_vehicle_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loaded_vehicle_timestamp', models.DateTimeField()),
                ('loaded_vehicle_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gunnybag_count', models.PositiveIntegerField()),
                ('gunnybag_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produce_gross_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('procurement_transaport_incharge_kyc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procurement_date', models.DateField()),
                ('produce_net_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_to_wallet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_to_agent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procurement_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procurement_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementProduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementTransactionMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Procurement')),
                ('transaction_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.AgentTransactionLog')),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementTransportInchargeKyc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=13)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionApprovalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionChequeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=150)),
                ('branch_name', models.CharField(max_length=100)),
                ('ifsc_code', models.CharField(max_length=100)),
                ('micr_code', models.CharField(blank=True, max_length=100, null=True)),
                ('account_holder_name', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=50)),
                ('date_of_issue', models.DateField()),
                ('cheque_number', models.PositiveIntegerField()),
                ('is_cleared', models.BooleanField(default=False)),
                ('cheque_cleared_date', models.DateField(blank=True, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_from', models.CharField(max_length=50)),
                ('payment_to', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='inputiteminputbatchagentinventory',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inputiteminputbatchmap',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inputpart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procurementgroup',
            name='procurement_produce',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.ProcurementProduce'),
        ),
        migrations.AddField(
            model_name='procurementgroup',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Season'),
        ),
        migrations.AddField(
            model_name='procurementgroup',
            name='unit_for_pricing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_per_for_price_calculation', to='inputdistri.Unit'),
        ),
        migrations.AddField(
            model_name='inputdistributiontransactionmap',
            name='input_item_sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputItemInputBatchAgentInventory'),
        ),
        migrations.AddField(
            model_name='inputdistributiontransactionmap',
            name='transaction_log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.AgentTransactionLog'),
        ),
        migrations.AddField(
            model_name='agenttransactionlog',
            name='cheque_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inputdistri.TransactionChequeDetails'),
        ),
        migrations.AddField(
            model_name='agenttransactionlog',
            name='data_entered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_initiated_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agenttransactionlog',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_log_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agenttransactionlog',
            name='transaction_approval_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.TransactionApprovalStatus'),
        ),
        migrations.AddField(
            model_name='agenttransactionlog',
            name='transaction_direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.TransactionDirection'),
        ),
        migrations.AddField(
            model_name='agenttransactionlog',
            name='transaction_mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.TransactionMode'),
        ),
    ]
