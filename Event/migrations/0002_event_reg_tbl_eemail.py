# Generated by Django 4.1.6 on 2023-04-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_reg_tbl',
            name='eemail',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
