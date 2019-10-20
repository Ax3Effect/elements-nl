from django.shortcuts import render
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
import csv
import io
import requests
import tempfile
from django.core import files
from PIL import Image
from django.utils.six import StringIO, BytesIO

from api.models import UploadedCSV, Data
from elements import settings

# Create your views here.
def home(request):
    return "Home page"

IGNORE_EMPTY_IMAGE = False

class CsvUploadView(APIView):
    parser_classes = [MultiPartParser]

    def parse_row(self, row, csv_model):
        title = row.get("title", None)
        description = row.get("description", None)
        image = row.get("image", None)

        data = Data(csv=csv_model, title=title, description=description, image=None, image_url=image)
        data.save()
        if image:
            request = requests.get(image, stream=True)
            if request.status_code != requests.codes.ok:
                uploaded_image, file_name = None, None
                return "image can't be downloaded"
            else:
                file_name = "{}_{}".format(data.id, image.split('/')[-1])
                lf = tempfile.NamedTemporaryFile()
                for block in request.iter_content(1024 * 8):
                    if not block:
                        break
                    lf.write(block)

                try:
                    img = Image.open(lf)
                except Exception:
                    return "image can't be opened"
                    pass
                else:
                    width_percent = (settings.BASEWIDTH/float(img.size[0]))
                    height_size = int((float(img.size[1])*float(width_percent)))
                    resize_img = img.resize((settings.BASEWIDTH, height_size), Image.ANTIALIAS)
                    resized = BytesIO()
                    resize_img.save(resized, format='JPEG', quality=90)
                    uploaded_image = files.File(resized)
                    data.image.save(file_name, uploaded_image)
                    return "success"
     

    def put(self, request, format=None):
        csv_file = request.data['file']
        csv_file.seek(0)
        reader = csv.DictReader(io.StringIO(csv_file.read().decode('utf-8'))) 

        csv_model = UploadedCSV(user=None)
        csv_model.save()

        upload_results = []

        for id, row in enumerate(reader):
            upload_result = self.parse_row(row, csv_model)
            upload_results.append({"id":id, "result":result})

        
        return Response(results)
