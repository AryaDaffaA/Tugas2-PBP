from django.test import TestCase, Client
from django.urls import resolve
from .views import index

class ContohAppTest(TestCase):
    def test_contoh_app_url_exist(self):
        response = Client().get('/contohapp')
        self.asserEqual(response.status_code, 200)

    def test_contoh_app_url_exist(self):
        response = Client().get('/contohapp')
        self.asserEqual(response.status_code, 200)

    def test_contoh_app_url_exist(self):
        response = Client().get('/contohapp')
        self.asserEqual(response.status_code, 200)

# Create your tests here.
