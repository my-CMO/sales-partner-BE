from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    # transcript = models.TextField()

    def __str__(self):
        return self.title

class Recording(models.Model):
    # meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='recordings')
    audio_file = models.FileField(upload_to='recordings/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recording of {self.meeting.title}"