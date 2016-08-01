"""Functional tests of the API."""
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from rest_framework import status


class TestPage(TestCase):

   def setUp(self):
       self.client = Client()

   def test_map_page(self):
       url = reverse('heatmap')
       response = self.client.get(url)
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertTemplateUsed(response, 'map.html')
       self.assertContains(response, 'Welcome to the IPv6 Heatmap application')
       self.assertEqual(response.context['data'] , 'test')