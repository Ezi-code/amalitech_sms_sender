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
    is_template = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-timestamp",)

    def __str__(self):
        return self.title


class MessageHistory(models.Model):
    message = models.ForeignKey(Messages, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-timestamp",)

    def __str__(self):
        return self.message.title


@receiver(post_save, sender=Messages)
def history_post_save_receiver(sender,instance, created, **kwargs):
    if created:
        MessageHistory.objects.create(message=instance)
