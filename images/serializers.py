from .models import images
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields = '__all__'