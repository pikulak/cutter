
from uuid import UUID
from celery import shared_task
from .models import FileAudio


@shared_task
def async_cut_file(file_id):
    processed_file = FileAudio.objects.get(pk=UUID(file_id))
    print("Processing file...")
