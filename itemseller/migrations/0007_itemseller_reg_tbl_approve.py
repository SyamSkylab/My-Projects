# Generated by Django 4.1.6 on 2023-04-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemseller', '0006_alter_product_upload_tbl_sellerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemseller_reg_tbl',
            name='Approve',
            field=models.BooleanField(default=False),
        ),
    ]