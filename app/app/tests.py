"""
Sample tests
"""

from django.test import SimpleTestCase
from . import calc


class TestCalculator(SimpleTestCase):
    """Test the calc module"""
    def test_add(self):
        """Test the add function"""
        res = calc.add(10, 9)
        self.assertEqual(res, 19)

    def test_subtract(self):
        """Test the subtract function"""
        res = calc.subtract(10, 9)
        self.assertEqual(res, 1)
