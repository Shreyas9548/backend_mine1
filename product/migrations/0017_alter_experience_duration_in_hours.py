# Generated by Django 4.1 on 2024-08-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_experience_slot_timing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='duration_in_hours',
            field=models.IntegerField(blank=True),
        ),
    ]