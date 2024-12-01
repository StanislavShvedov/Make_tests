import unittest
from vote import vote
from unittest import TestCase


class TestMain(TestCase):
    def test_vote_with_params(self):
        for i, (nums_list, expected) in enumerate([
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2),
            ([3, 3, 3, 2, 2], 2)
        ]):
            with self.subTest(i):
                result = vote(nums_list)
                self.assertEqual(expected, result)
