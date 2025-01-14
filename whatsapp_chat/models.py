from django.db import models
from tenant.models import Tenant 
from contacts.models import Contact
class Conversation(models.Model):
    contact_id = models.CharField(max_length=255)
    message_text = models.TextField()
    sender = models.CharField(max_length=50)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    source=models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add any other fields you may need

    # Assuming you have tenant-specific tables, add a foreign key to connect them
    # tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Conversation ID: {self.id}, Contact ID: {self.contact_id}, Sender: {self.sender}"
class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Contact, related_name='groups')
    date_created = models.DateTimeField(auto_now_add=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Group ID: {self.id}, Name: {self.name}, Members: {self.members.count()}"
