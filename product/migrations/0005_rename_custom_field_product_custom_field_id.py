# Generated by Django 4.1 on 2024-08-13 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_custom_fields_product_custom_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='custom_field',
            new_name='custom_field_id',
        ),
    ]
