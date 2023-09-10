"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalTests(SimpleTestCase):

# Test calc module
    def test_add_calculator(self):
        # Test the calculator method
        res = calc.add(5,5)

        self.assertEqual(res, 10)

    def test_subtract_number(self):
        # Test subtracting numbers
        res = calc.subtract(10,15)

        self.assertEqual(res, -5)