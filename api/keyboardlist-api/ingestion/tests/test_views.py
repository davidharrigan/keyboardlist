from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DataIngestionTests(APITestCase):
    ingestion_url = reverse('ingestion:ingest')
    valid_ingestion_data = {
        'manufacturer': 'Konami',
        'keyboard_model': 'Potato 3000',
        'keyboard_switch_type': 'Cherry MX Blue',
        'keyboard_size': 'Tenkeyless',
        'seller_name': 'Backstreet Boys',
        'seller_url': 'http://forthehomies.org',
        'seller_in_stock': '5+'
    }

    def test_post_valid_data(self):
        response = self.client.post(self.ingestion_url, self.valid_ingestion_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
