# Generated by Django 3.0.11 on 2021-07-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0004_coupon_top_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='short_description',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
