# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-23 07:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instance', '0035_auto_20210213_0649'),
        ('inputdistri', '0030_auto_20210223_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InputCombo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.AreaCv')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Business')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_item_created_by_instance', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_item_modified_by_instance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InputGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('number_of_units', models.PositiveIntegerField()),
                ('unit_quantity', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity_at_receipt', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity_now', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity_now_time', models.DateTimeField()),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_of_receipt', models.DateField()),
                ('date_of_manufacturing', models.DateField()),
                ('date_of_expiry', models.DateField()),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instance.Business')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_batch_created_by_instance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InputGoodsCodeBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_digit', models.PositiveIntegerField()),
                ('input_code_prefix', models.CharField(max_length=5)),
                ('input_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputType')),
            ],
        ),
        migrations.CreateModel(
            name='InputGoodsExpiryDateTrace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_expiry', models.DateField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('changed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('input_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputGoods')),
            ],
        ),
        migrations.CreateModel(
            name='InputName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_code', models.CharField(max_length=10)),
                ('input_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputType')),
            ],
        ),
        migrations.CreateModel(
            name='InputPacketInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packet_code', models.CharField(max_length=10)),
                ('quantity_at_receipt', models.PositiveIntegerField()),
                ('quantity_now', models.PositiveIntegerField()),
                ('quantity_now_time', models.DateTimeField()),
                ('price_per_packet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_of_expiry', models.DateField()),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_item_input_batch_map_created_by_instance', to=settings.AUTH_USER_MODEL)),
                ('input_combo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputCombo')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_item_input_batch_modified_by_instance', to=settings.AUTH_USER_MODEL)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='InputPacketInventoryExpiryDateTrace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_expiry', models.DateField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('changed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('input_packet_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputPacketInventory')),
            ],
        ),
        migrations.CreateModel(
            name='InputPacketInventoryLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_prefix', models.CharField(max_length=10)),
                ('label_suffix', models.CharField(max_length=10)),
                ('label_range_start', models.PositiveIntegerField()),
                ('label_range_end', models.PositiveIntegerField()),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('input_packet_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputPacketInventory')),
            ],
        ),
        migrations.CreateModel(
            name='InputPacketInventoryPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('input_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputGoods')),
                ('input_packet_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputPacketInventory')),
            ],
        ),
        migrations.CreateModel(
            name='InputPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, max_digits=8)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_part_created_by_instance', to=settings.AUTH_USER_MODEL)),
                ('input_combo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputCombo')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_part_modified_by_instance', to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputName')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='InputStockStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InputStoreInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(blank=True, max_length=250, null=True)),
                ('sub_section', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_receipt', models.DateField()),
                ('quantity_at_receipt', models.PositiveIntegerField()),
                ('quantity_now', models.PositiveIntegerField()),
                ('quantity_now_time', models.DateTimeField()),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_storage_location_map_created_by_instance', to=settings.AUTH_USER_MODEL)),
                ('input_packet_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputPacketInventory')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_storage_location_batch_modified_by_instance', to=settings.AUTH_USER_MODEL)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Storage')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='InputStoreInventoryPacketLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('received_date', models.DateTimeField()),
                ('dispatched_date', models.DateTimeField(blank=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('dispatched_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input_batch_packet_labeled_dispatched_by_instance', to=settings.AUTH_USER_MODEL)),
                ('input_store_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputStoreInventory')),
                ('received_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_batch_packet_labeled_recieved_by_instance', to=settings.AUTH_USER_MODEL)),
                ('stock_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputStockStatus')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='inputpacketinventorypart',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputPart'),
        ),
        migrations.AddField(
            model_name='inputgoods',
            name='input_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.InputName'),
        ),
        migrations.AddField(
            model_name='inputgoods',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_batch_modified_by_instance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inputgoods',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Supplier'),
        ),
        migrations.AddField(
            model_name='inputgoods',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputdistri.Unit'),
        ),
    ]