# Generated by Django 4.2.1 on 2024-05-15 08:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("tenant", "0001_initial"),
        ("accounts", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="tenant",
            field=models.ForeignKey(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                to="tenant.tenant",
            ),
            preserve_default=False,
        ),
    ]