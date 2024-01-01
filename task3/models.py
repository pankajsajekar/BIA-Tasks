from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.title}'