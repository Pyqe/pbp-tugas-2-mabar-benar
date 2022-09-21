from django.test import TestCase
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('html/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('xml/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('json/')
        self.assertEqual(response.status_code, 200)