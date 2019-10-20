from django.contrib import admin
from api.models import UploadedCSV, Data

# Register your models here.
admin.site.register(UploadedCSV)
admin.site.register(Data)