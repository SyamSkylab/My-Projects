# Generated by Django 4.1.6 on 2023-04-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0005_alter_slot_tbl_etime'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot_tbl',
            name='status',
            field=models.CharField(default='no issues', max_length=50),
        ),
    ]