# Generated by Django 4.1 on 2024-06-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('leads_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('revenue', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_leads', models.IntegerField(default=0)),
            ],
        ),
    ]