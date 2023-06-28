# Generated by Django 4.1.8 on 2023-04-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0020_product_details_cart1"),
    ]

    operations = [
        migrations.CreateModel(
            name="sales_details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seller_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="user_details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=20)),
                ("phone", models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name="Customer1",
        ),
    ]
