# Generated by Django 4.1.6 on 2023-04-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0002_turf_reg_tbl_timg'),
    ]

    operations = [
        migrations.AddField(
            model_name='turf_reg_tbl',
            name='tdetails',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
