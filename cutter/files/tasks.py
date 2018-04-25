import os
from uuid import UUID
from celery import shared_task
from django.core.files import File
from .models import FileAudio, TempFile, processed_audio_file_path
from .utils import ensure_dir_exists


@shared_task
def async_cut_file(temp_file_id, preprocessed_file_id):
    processed_file = FileAudio.objects.get(pk=UUID(preprocessed_file_id))
    temp_file = TempFile.objects.get(pk=UUID(temp_file_id))

    processed_file_path = processed_audio_file_path(processed_file,
                                                    processed_file.original_filename)
    ensure_dir_exists(os.path.dirname(processed_file_path))

    with File(open(temp_file.upload.path, 'rb')) as file:
        # process file here ...
        processed_file.upload.save(name='', content=file)

    temp_file.delete()
