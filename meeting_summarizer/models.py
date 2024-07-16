from django.db import models

class Recording(models.Model):
    audio_file = models.FileField(upload_to='Media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    participant_count = models.IntegerField()

class Transcript(models.Model):
    recording = models.ForeignKey(Recording, related_name='transcripts', on_delete=models.CASCADE)
    speaker = models.CharField(max_length=10)
    text = models.TextField()

