from django.db import models
from datetime import date

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    author_name = models.CharField(max_length=100, blank=False, null=True)
    publication_date = models.DateField(("Publication date"), auto_now=False, auto_now_add=False, blank=True, null=True)
    createdDate = models.DateField(("Created Date"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    