# Generated by Django 4.1 on 2024-08-14 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=64)),
                ('model_name', models.CharField(choices=[('LEAD', 'lead'), ('OPPORTUNITY', 'opportunity')], max_length=20)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant')),
            ],
        ),
    ]