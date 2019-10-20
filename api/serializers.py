from rest_framework import serializers
from api.models import UploadedCSV, Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id', 'title', 'description', 'image', 'image_url']

class UploadedCSVSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True, read_only=True)

    class Meta:
        model = UploadedCSV
        fields = ['id', 'data', 'created_at', 'updated_at']