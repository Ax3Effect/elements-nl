
from django.shortcuts import render
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
import csv
import io
from .models import UploadedCSV, Data

# Create your views here.
def home(request):
    return "Home page"


class CsvUploadView(APIView):
    parser_classes = [MultiPartParser]

    def put(self, request, format=None):
        csv_file = request.data['file']
        csv_file.seek(0)
        reader = csv.DictReader(io.StringIO(csv_file.read().decode('utf-8'))) 
        for row in reader:
            print(row)

        return Response(status=204)
