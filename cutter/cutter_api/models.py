import uuid

from django.db import models
from .utils import sha256_checksum


class File(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    upload = models.FileField(
        upload_to=lambda instance, _: f'files/{instance.uuid}'
    )
    sha256 = models.CharField(max_length=60)

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if is_new:
            self.sha256 = sha256_checksum(self.upload.path)
        super().save(*args, **kwargs)


class FileAudio(File):
    pass

