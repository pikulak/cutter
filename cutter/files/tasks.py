from uuid import UUID
from celery import shared_task
from .models import FileAudio
from pydub import AudioSegment


@shared_task
def async_cut_file(file_id):
    file = FileAudio.objects.get(pk=UUID(file_id))
    song = AudioSegment.from_mp3(file.upload.path)
    song_after_slice = song[:10*1000]
    song_after_slice.export(file.upload.path)
    print("Processing file...")
