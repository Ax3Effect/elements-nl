from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

urlpatterns = [
    path('upload/', views.CsvUploadView.as_view()),
]