# Generated by Django 4.1.7 on 2023-04-14 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_temporaryvoucher_alter_vouchers_voucherid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchers',
            name='dateOfAcquire',
            field=models.DateField(verbose_name=datetime.datetime(2023, 4, 14, 15, 2, 3, 388970)),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='dateOfExpiry',
            field=models.DateField(verbose_name=datetime.datetime(2023, 4, 14, 15, 2, 3, 388970)),
        ),
    ]