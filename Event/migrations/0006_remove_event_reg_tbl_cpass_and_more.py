# Generated by Django 4.1.6 on 2023-04-11 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0005_event_reg_tbl_avl_tickets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_reg_tbl',
            name='cpass',
        ),
        migrations.RemoveField(
            model_name='event_reg_tbl',
            name='pass1',
        ),
    ]