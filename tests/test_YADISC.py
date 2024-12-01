import unittest
from unittest import TestCase
import requests
from YADisc import TOKEN


class TestYADisc(TestCase):
    def setUp(self):
        self.headers = {
            'Authorization': TOKEN
        }

        self.params = {
            'path': f'/Image'
        }

    def test_connection_YADisc(self):
        result = requests.get('https://cloud-api.yandex.net/v1/disk', headers=self.headers)
        self.assertEqual(result.status_code, 200)

    def test_create_folder(self):
        for i, staus in enumerate([
            201,
            409,
        ]):
            with self.subTest(i):
                result = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                      params=self.params,
                                      headers=self.headers)

                self.assertEqual(result.status_code, staus)
