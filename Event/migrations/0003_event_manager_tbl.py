# Generated by Django 4.1.6 on 2023-04-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_event_reg_tbl_eemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_manager_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.IntegerField()),
                ('Address', models.TextField()),
                ('pass1', models.CharField(max_length=25)),
                ('pass2', models.CharField(max_length=25)),
            ],
        ),
    ]
