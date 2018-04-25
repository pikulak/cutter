from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import (
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
