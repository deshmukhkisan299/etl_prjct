# Generated by Django 4.1.8 on 2023-05-01 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0031_alter_sales_detailss_buyer_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_model",
            old_name="name",
            new_name="username",
        ),
    ]
