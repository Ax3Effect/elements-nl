from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class UploadedCSV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Data(models.Model):
    csv = models.ForeignKey(UploadedCSV, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    image = models.FileField(blank=True, null=True)
    image_url = models.URLField(max_length=400)