# Generated by Django 3.0.11 on 2021-03-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='photo',
        ),
        migrations.AddField(
            model_name='coupon',
            name='photos',
            field=models.ManyToManyField(to='coupons.Image'),
        ),
    ]
