# Generated by Django 3.0.11 on 2021-03-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20210306_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='price_before',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='price_now',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
