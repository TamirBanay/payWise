# Generated by Django 4.1.7 on 2023-04-11 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_temporaryvoucher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temporaryvoucher',
            old_name='usage_limit',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='temporaryvoucher',
            old_name='voucher_code',
            new_name='storeName',
        ),
    ]