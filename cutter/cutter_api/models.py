import uuid

from django.db import models


class File(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    upload = models.FileField(
        upload_to=lambda instance, _: f'files/{instance.uuid}'
    )
    sha265 = models.CharField(max_length=60)


class FileAudio(File):
    pass

