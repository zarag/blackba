# Generated by Django 3.0.11 on 2021-02-28 21:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0002_auto_20210228_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', tinymce.models.HTMLField()),
                ('photo', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='coupon-avatars')),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
            ],
        ),
    ]
