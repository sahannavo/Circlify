"""Unit tests for calculator logic"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from circlify.core.calculator import CircleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = CircleCalculator()
    
    def test_diameter(self):
        self.assertEqual(self.calc.calculate_diameter(5), 10)
        self.assertEqual(self.calc.calculate_diameter(2.5), 5)
    
    def test_circumference(self):
        self.assertAlmostEqual(self.calc.calculate_circumference(1), 6.283185, places=5)
    
    def test_area(self):
        self.assertAlmostEqual(self.calc.calculate_area(1), 3.14159265, places=5)
    
    def test_format_result(self):
        self.assertEqual(self.calc.format_result(0.001), "0.001000")
        self.assertEqual(self.calc.format_result(0.5), "0.5000")
        self.assertEqual(self.calc.format_result(100), "100.00")
        self.assertEqual(self.calc.format_result(5000), "5000.0")

if __name__ == '__main__':
    unittest.main()