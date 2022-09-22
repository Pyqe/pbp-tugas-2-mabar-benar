from django.test import TestCase
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)