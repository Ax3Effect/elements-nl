from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register(r'data', views.DataViewSet, base_name="data")

urlpatterns = [
    path('upload/', views.CsvUploadView.as_view(), name='csv-upload'),
    path('', include(router.urls)),
]