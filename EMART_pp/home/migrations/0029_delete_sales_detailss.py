# Generated by Django 4.1.8 on 2023-04-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0028_remove_sales_detailss_seller_id_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="sales_detailss",
        ),
    ]
