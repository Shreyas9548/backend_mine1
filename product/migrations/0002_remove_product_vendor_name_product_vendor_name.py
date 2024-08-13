# Generated by Django 4.1 on 2024-07-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendors", "0001_initial"),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="vendor_name",
        ),
        migrations.AddField(
            model_name="product",
            name="vendor_name",
            field=models.ManyToManyField(
                blank=True, related_name="products", to="vendors.vendors"
            ),
        ),
    ]
