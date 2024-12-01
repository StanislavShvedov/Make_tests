import unittest
from unittest import TestCase
from secretary import get_name, get_directory, add, directories, documents


class TestSecretary(TestCase):
    def test_get_name_with_params(self):
        for i, (num, expected) in enumerate([
            ("2207 876234", "Василий Гупкин"),
            ("123234", "Документ не найден")
        ]):
            with self.subTest(i):
                result = get_name(num)
                self.assertEqual(result, expected)

    def test_get_dir_with_params(self):
        for i, (num, expected) in enumerate([
            ("2207 876234", "1"),
            ("123234", "Полки с таким документом не найдено")
        ]):
            with self.subTest(i):
                result = get_directory(num)
                self.assertEqual(result, expected)

    def test_add_with_params(self):
        for i, (document_type, number, name, shelf_number, expected) in enumerate([
            ("passport", "1", "Petya Petrov", "4", "Добавлен новый документ"),
        ]):
            with self.subTest(i):
                result = add(document_type, number, name, shelf_number)
                self.assertEqual(result, expected)
                self.assertEqual(len(documents), 5)
                self.assertEqual(len(directories), 4)
