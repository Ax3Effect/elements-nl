from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class UploadedCSV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} CSV Parent - {} entities ({})".format(self.id, self.data.count(), self.created_at)

    class Meta:
        verbose_name = "CSV Parent"
        verbose_name_plural = "CSV Parents"

class Data(models.Model):
    csv = models.ForeignKey(UploadedCSV, on_delete=models.CASCADE, related_name="data", verbose_name="CSV Parent")
    title = models.CharField(max_length=400, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    image = models.ImageField(upload_to="cached/", blank=True, null=True, verbose_name="Cached image")
    image_url = models.URLField(max_length=400, verbose_name="Original image URL")

    def __str__(self):
        return "{} {} {:20}".format(self.id, self.title, self.description)

    class Meta:
        verbose_name = "CSV Data"
        verbose_name_plural = "CSV Data"