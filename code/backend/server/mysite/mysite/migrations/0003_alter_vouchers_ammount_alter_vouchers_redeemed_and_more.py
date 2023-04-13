# Generated by Django 4.1.7 on 2023-04-11 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_vouchers_ammount_alter_vouchers_redeemed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchers',
            name='ammount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='redeemed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='storeType',
            field=models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.storetype'),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='voucherCategory',
            field=models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.vouchercategory'),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='voucherID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='walletID',
            field=models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.wallet'),
        ),
    ]
