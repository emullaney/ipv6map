"""Functional tests of the API."""
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status

from ..models import ipv6Address


class ipv6AddressAPITestCase(TestCase):
    """Examples of the MSO API endpoint functionality."""

    def setUp(self):
        self.url = reverse('ipv6address-list')
        for num in range(1000, 1011):
            ipv6Address.objects.create(
                latitude = num,
                longitude = num*2
            )

    def test_filter(self):
        """Filter ipv6 address queryset."""
        # Should return 4 addresses
        data = {
            'min_latitude': 1005,
            'max_latitude': 1010,
            'min_longitude': 2012,
            'max_longitude': 2018
        }
        response = self.client.get(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(len(response.data), 4)

        #self.assertEqual(data['results'][0]['id'], test_asset.id)
