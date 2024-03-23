from django.db import models
import uuid
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save


# Create your models here.


class Messages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    title = models.CharField(max_length=150, null=True)
    content = models.TextField()
    recipients = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-sent_at"]

    def __str__(self):
        return f"{self.title} >> {self.sent_at}"


class MessageHistory(models.Model):
    message = models.ForeignKey(Messages, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message.title


@receiver(post_save, sender=Messages)
def save_message_history(sender, instance, created, **kwargs):
    if created:
        MessageHistory.objects.create(message=instance)


class Templates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    recipients = models.TextField(default=None)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
