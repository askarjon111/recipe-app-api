from django.test import TestCase
from .calc import add, subtract


class CalcTests(TestCase):

    def test_add_two_numbers(self):
        """Test"""
        self.assertEqual(add(3,8), 11)

    def test_subtract_numbers(self):
        """Test"""
        self.assertEqual(subtract(5,11), 6)