import os


class SignalDeleteFile:

    @staticmethod
    def delete_file_on_change(sender, instance, field):
        if not instance.pk:
            return False
        try:
            old_file = getattr(sender.objects.get(pk=instance.pk), field)
        except sender.DoesNotExist:
            return False

        new_file = getattr(instance, field)
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)

    @staticmethod
    def delete_file_on_delete(sender, instance, field):
        file_field = getattr(instance, field)
        if file_field:
            if os.path.isfile(file_field.path):
                os.remove(file_field.path)
