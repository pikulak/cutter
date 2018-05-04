import os
import uuid
import shutil

from django.db import models


def default_file_path(instance, filename):
    return f'default/{instance.id}/{filename}'


def audio_file_path(instance, filename):
    return f'processed/audio/{instance.id}/{filename}'


class BaseFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    upload = models.FileField(upload_to=default_file_path)
    sha256 = models.CharField(max_length=60, blank=True)

    class Meta:
        abstract = True


class FileMetadataMixin(models.Model):
    original_filename = models.CharField(max_length=64, blank=True)

    class Meta:
        abstract = True


class FileAudio(BaseFile, FileMetadataMixin):
    upload = models.FileField(upload_to=audio_file_path)

    def delete(self, *args, **kwargs):
        if self.upload:
            dir_path = os.path.dirname(self.upload.path)
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)
        super().delete(*args, **kwargs)
