from .models import FileAudio
from rest_framework import serializers


class FileAudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileAudio
        fields = ('id', 'upload', 'processing_state')
        read_only_fields = ('processing_state',)
