# Generated by Django 4.1.8 on 2023-04-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0029_delete_sales_detailss"),
    ]

    operations = [
        migrations.CreateModel(
            name="sales_detailss",
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
                ("record_date", models.DateField()),
                ("buyer_id", models.IntegerField()),
                ("product_id", models.IntegerField()),
                ("prd_quant", models.IntegerField()),
            ],
        ),
    ]
