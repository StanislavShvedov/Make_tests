import unittest
from unittest import TestCase
from names import fio


class TestName(TestCase):
    def test_name_with_params(self):
        for i, (fio_list, expexted) in enumerate([
            (['Иванов', 'Иван', 'Иванович'], 'ИИИ'),
            (['Petrov', 'Petr', 'Petrovich'], 'PPP'),
        ]):
            with self.subTest(i):
                result = fio(fio_list)
                self.assertEqual(result, expexted)
