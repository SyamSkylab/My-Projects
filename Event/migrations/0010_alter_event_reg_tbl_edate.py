# Generated by Django 4.1.6 on 2023-04-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0009_event_reg_tbl_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_reg_tbl',
            name='edate',
            field=models.DateTimeField(),
        ),
    ]
