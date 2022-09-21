from django.test import TestCase, Client
from django.urls import resolve

class ContohAppTest(TestCase):
    def test_html_url_exist(self):
        response = Client().get('https://tugas2-pbp-arya.herokuapp.com/mywatchlist/')
        self.assertEqual(response.status_code, 200)

    def test_xml_url_exist(self):
        response = Client().get('https://tugas2-pbp-arya.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json_url_exist(self):
        response = Client().get('https://tugas2-pbp-arya.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
