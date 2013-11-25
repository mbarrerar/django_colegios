from django.test import TestCase
from .models import Colegios
from django.test import Client

class ColegioTest(TestCase):

	def test_view(self):
		c = Client()
		response = c.get('/colegios/index')
		self.assertEqual(response.status_code,200)