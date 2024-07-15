from rest_framework.viewsets import ModelViewSet
from .models import Meeting, Recording
from .serializer import MeetingSerializer, RecordingSerializer

class MeetingViewSet(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class RecordingViewSet(ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer
