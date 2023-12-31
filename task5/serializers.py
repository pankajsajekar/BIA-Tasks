from rest_framework import serializers

from task5.models import UploadedVideo

class UploadedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedVideo
        fields = '__all__'

    def create(self, validated_data):
        return UploadedVideo.objects.create(**validated_data)