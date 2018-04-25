from rest_framework.viewsets import(
    GenericViewSet,
    mixins
)
from .models import FileAudio
from .serializers import FileAudioSerializer


class FileViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FileAudio.objects.all()
    serializer_class = FileAudioSerializer
