# Generated by Django 4.1.6 on 2023-04-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0004_event_reg_tbl_emid'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_reg_tbl',
            name='avl_tickets',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
