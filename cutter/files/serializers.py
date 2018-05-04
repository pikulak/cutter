from .models import FileAudio
from rest_framework import serializers


class FileAudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileAudio
        fields = ('id', 'upload')
