# Generated by Django 4.1.6 on 2023-04-27 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0003_turf_reg_tbl_tdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='slot_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stime', models.TimeField()),
                ('etime', models.TextField()),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Turf.turf_reg_tbl')),
            ],
        ),
    ]