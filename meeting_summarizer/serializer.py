from rest_framework import serializers
from .models import Meeting, Recording

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id', 'title', 'date']

class RecordingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recording
        fields = ['id', 'audio_file', 'uploaded_at']

    # def create(self, validated_data):
    #     meeting_title = validated_data.pop('meeting_title')
    #     meeting, created = Meeting.objects.get_or_create(title=meeting_title)
    #     recording = Recording.objects.create(meeting=meeting, **validated_data)
    #     return recording
