# Generated by Django 4.1.6 on 2023-04-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0007_turf_reg_tbl_tloc'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot_tbl',
            name='amount',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]