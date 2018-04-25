from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import (
    GenericViewSet,
    mixins
)
from .models import FileAudio, TempFile
from .serializers import FileAudioSerializer
from .tasks import async_cut_file


class FileViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FileAudio.objects.all()
    serializer_class = FileAudioSerializer

    @staticmethod
    def _create_temp_file(file):
        temp_file = TempFile(upload=file)
        temp_file.save()
        return temp_file

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        original_filename = serializer.validated_data['upload'].name
        temp_file = self._create_temp_file(serializer.validated_data['upload'])

        serializer.validated_data['temp_file'] = temp_file
        serializer.validated_data['original_filename'] = original_filename
        serializer.validated_data['upload'] = None

        preprocessed_file = serializer.save()
        async_cut_file.delay(temp_file.pk, preprocessed_file.pk)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
