

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("meetings", "0002_remove_meetings_from_remove_meetings_to_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meetings",
            name="assigned_to",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="meeting_assigned_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="meetings",
            name="createdBy",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="meeting_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
