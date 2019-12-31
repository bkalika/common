from http import HTTPStatus

import requests
from django.test import Client, TestCase
from django.urls import reverse

from .settings import PRIVAT_API


class StatusView(TestCase):
    client = Client()

    def test_status_view(self):
        response = self.client.get(reverse('health_check'))
        assert response.status_code == HTTPStatus.OK

    def test_usd(self):
        response = self.client.get(reverse('usd'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["ccy"], 'USD')
        assert response.status_code == HTTPStatus.OK

    def test_eur(self):
        response = self.client.get(reverse('eur'))
        self.assertEqual(response.context["ccy"], 'EUR')
        assert response.status_code == HTTPStatus.OK

    def test_rur(self):
        response = self.client.get(reverse('rur'))
        self.assertEqual(response.context["ccy"], 'RUR')
        assert response.status_code == HTTPStatus.OK

    def test_connect_to_the_api(self):
        try:
            requests.get(f'{PRIVAT_API}')
            return True
        except requests.ConnectionError:
            self.assertRaises(ConnectionError)
