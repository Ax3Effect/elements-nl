from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase, APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.

class TestAPIUpload(TestCase):
    client_class = APIClient

    def test_csv_is_accepted(self):
        file = SimpleUploadedFile("test.csv", open('test_data/test.csv', 'rb').read() )
        payload = {'file':file}
        response = self.client.put('/api/upload/', payload, format='multipart')
        self.assertEqual(response.status_code, 201)

    def test_invalid_csv_is_unaccepted(self):
        file = SimpleUploadedFile("test.csv", open('test_data/test_invalid.csv', 'rb').read() )
        payload = {'file':file}
        response = self.client.put('/api/upload/', payload, format='multipart')
        self.assertEqual(response.status_code, 422)

    def test_blank_is_unaccepted(self):
        file = SimpleUploadedFile("blank", open('test_data/blank', 'rb').read() )
        payload = {'file':file}
        response = self.client.put('/api/upload/', payload, format='multipart')
        self.assertEqual(response.status_code, 422)

    def test_no_input_is_unaccepted(self):
        response = self.client.put('/api/upload/')
        self.assertEqual(response.status_code, 404)

    def test_parse(self):
        file = SimpleUploadedFile("test.csv", open('test_data/test.csv', 'rb').read() )
        payload = {'file':file}
        response = self.client.put('/api/upload/', payload, format='multipart')
        data = response.data
        self.assertEqual(data["uploaded_result"][0]["result"], "image can't be downloaded")
        self.assertEqual(data["uploaded_result"][1]["result"], "success")
        self.assertEqual(data["uploaded_result"][2]["result"], "image can't be opened")
        self.assertEqual(data["uploaded_result"][3]["result"], "no url")