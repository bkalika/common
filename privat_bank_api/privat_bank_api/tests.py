from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse


class StatusView(TestCase):
    client = Client()

    def test_status_view(self):
        response = self.client.get(reverse('health_check'))
        assert response.status_code == HTTPStatus.OK

    def test_usd(self):
        response = self.client.get(reverse('usd'))
        assert response.status_code == HTTPStatus.OK

    def test_eur(self):
        response = self.client.get(reverse('eur'))
        assert response.status_code == HTTPStatus.OK

    def test_rur(self):
        response = self.client.get(reverse('rur'))
        assert response.status_code == HTTPStatus.OK

    def test_usd2(self):
        response = self.client.get(reverse('usd'))
        assert response.url == "http://127.0.0.1:8000/usd/"
