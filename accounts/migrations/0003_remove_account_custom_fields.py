# Generated by Django 4.1 on 2024-08-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='custom_fields',
        ),
    ]
