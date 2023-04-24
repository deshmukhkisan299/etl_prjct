# Generated by Django 4.1.8 on 2023-04-18 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cart_model_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product_cost', models.IntegerField(default=0)),
                ('Product_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart_model',
        ),
    ]
