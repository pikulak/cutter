import uuid

from django.db import models
from .utils import sha256_checksum


def upload_file_path(instance, filename):
    return f'uploaded/{instance.id}/{filename}'


class File(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    upload = models.FileField(upload_to=upload_file_path)
    sha256 = models.CharField(max_length=60, blank=True)


class FileAudio(File):
    pass
