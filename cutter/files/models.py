import os
import uuid
import shutil

from django.db import models


def default_file_path(instance, filename):
    return f'default/{instance.id}/{filename}'


def temp_file_path(instance, _):
    return f'tmp/{instance.id}/'


def processed_audio_file_path(instance, filename):
    return f'processed/audio/{instance.id}/{filename}'


class BaseFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    upload = models.FileField(upload_to=default_file_path)
    sha256 = models.CharField(max_length=60, blank=True)

    class Meta:
        abstract = True


class TempFile(BaseFile):
    upload = models.FileField(upload_to=temp_file_path)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.upload.path):
            os.remove(self.upload.path)

        super().delete(*args, **kwargs)


class FileAudio(BaseFile):
    upload = models.FileField(upload_to=processed_audio_file_path, blank=True)
    temp_file = models.OneToOneField(TempFile, on_delete=models.CASCADE, blank=True)

    def delete(self, *args, **kwargs):
        dir_path = os.path.dirname(self.upload.path)
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

        self.temp_file.delete()
        super().delete(*args, **kwargs)
