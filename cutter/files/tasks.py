from uuid import UUID
from celery import shared_task
from .models import FileAudio


@shared_task
def async_cut_file(file_temp_path, file_id):
    file_obj = FileAudio.objects.get(pk=UUID(file_id))
    print(file_obj, file_temp_path)
