# Generated by Django 4.1.6 on 2023-04-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0006_slot_tbl_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='turf_reg_tbl',
            name='tloc',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]