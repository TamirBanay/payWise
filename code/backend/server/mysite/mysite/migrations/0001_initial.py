# Generated by Django 4.1.7 on 2023-03-22 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayWiseUser',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(blank=True, max_length=30, null=True)),
                ('houseNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('dateOfBirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('typeID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoucherCategory',
            fields=[
                ('categoryID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('walletID', models.IntegerField(primary_key=True, serialize=False)),
                ('userID', models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.paywiseuser')),
            ],
        ),
        migrations.CreateModel(
            name='Vouchers',
            fields=[
                ('voucherID', models.IntegerField(primary_key=True, serialize=False)),
                ('ammount', models.IntegerField()),
                ('dateOfAcquire', models.DateField()),
                ('dateOfExpiry', models.DateField()),
                ('redeemed', models.BooleanField(default=False)),
                ('storeType', models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.storetype')),
                ('voucherCategory', models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.vouchercategory')),
                ('walletID', models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('storeID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(blank=True, max_length=30, null=True)),
                ('houseNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('type', models.ForeignKey(default='undefined', max_length=30, on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.storetype')),
            ],
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('alertID', models.IntegerField(primary_key=True, serialize=False)),
                ('alertDate', models.DateField()),
                ('aletHour', models.TimeField()),
                ('voucherID', models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.vouchers')),
                ('walletID', models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.wallet')),
            ],
        ),
    ]
