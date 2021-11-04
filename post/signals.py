from django.db import models
from django.dispatch import receiver
from post.models import Article
from utils.helpers import SignalDeleteFile


@receiver(models.signals.pre_save, sender=Article)
def auto_delete_file_on_change(sender, instance, **kwargs):
    SignalDeleteFile.delete_file_on_change(
        sender, instance, sender.field_file_to_deleted())


@receiver(models.signals.post_delete, sender=Article)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    SignalDeleteFile.delete_file_on_delete(
        sender, instance, sender.field_file_to_deleted())
