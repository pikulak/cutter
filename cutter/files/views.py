from rest_framework import viewsets
from .models import FileAudio
from .serializers import FileAudioSerializer


class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FileAudio.objects.all()
    serializer_class = FileAudioSerializer
