from django.db import models

# Create your models here.

class UploadedVideo(models.Model):
    video = models.FileField(upload_to='uploads/')
    edited_video = models.FileField(upload_to='edited_videos/', null=True, blank=True)