from rest_framework import serializers
from .models import Transcript, Recording

class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcript
        fields = ['speaker', 'text']

class RecordingSerializer(serializers.ModelSerializer):
    transcripts = TranscriptSerializer(many=True, read_only=True)

    class Meta:
        model = Recording
        fields = ['id', 'audio_file', 'uploaded_at', 'participant_count', 'transcripts']
