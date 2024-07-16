from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Recording
from .serializer import RecordingSerializer
from .services import transcribe_audio
import threading


class RecordingUploadView(APIView):
    def post(self, request, format=None):
        serializer = RecordingSerializer(data=request.data)
        if serializer.is_valid():
            recording = serializer.save()
            response_data = serializer.data

            response = Response(response_data, status=status.HTTP_201_CREATED)

            # STT 변환 처리
            threading.Thread(target=transcribe_audio, args=(recording,)).start()

            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecordingViewSet(ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer


