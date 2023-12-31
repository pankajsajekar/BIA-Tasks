from rest_framework import serializers
from .models import Book


# Here I used ModelSerializer or we can go with serializer
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'publication_date']

    def create(self, validated_data):
        return super().create(validated_data)
    
