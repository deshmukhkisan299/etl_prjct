# Generated by Django 4.1.8 on 2023-04-26 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_alter_product1_seller_mob_no"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product1",
            name="Seller_mob_no",
        ),
    ]
