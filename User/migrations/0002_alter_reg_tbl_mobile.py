# Generated by Django 4.1.6 on 2023-03-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_tbl',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
