import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simplecrm.settings')
django.setup()

from django.contrib.contenttypes.models import ContentType

# Now you can access the ContentType framework
content_types = ContentType.objects.all()
for content_type in content_types:
    print(f"Model: {content_type.model}, ID: {content_type.id}")
