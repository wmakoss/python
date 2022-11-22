#!/usr/bin/python3
# coding=utf-8

from math import sqrt

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):             # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):        # obsługa point1 == point2
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        return sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertEqual(str(Point(4,3.598)), "(4, 3.598)")
        self.assertEqual(str(Point(-534.6543, -98435.543)), "(-534.6543, -98435.543)")

        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")
        self.assertEqual(repr(Point(4,3.598)), "Point(4, 3.598)")
        self.assertEqual(repr(Point(-534.6543, -98435.543)), "Point(-534.6543, -98435.543)")

    def test_cmp(self):         # Trzeba sprawdzać ==, !=
        self.assertTrue(Point(2, 2) == Point(2, 2))
        self.assertFalse(Point(2, 2) == Point(2, 3))
        self.assertTrue(Point(2, 2) != Point(2, 3))
        self.assertFalse(Point(2, 2) != Point(2, 2))

    def test_add(self):         # operator +
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))
        self.assertEqual(Point(1, 2) + Point(-3, -4), Point(-2, -2))
        self.assertEqual(Point(5, 3.2) + Point(-1, -1.1), Point(4, 2.1))

    def test_sub(self):         # operator -
        self.assertEqual(Point(1, 2) - Point(3, 4), Point(-2, -2))
        self.assertEqual(Point(1, 2) - Point(-3, -4), Point(4, 6))
        self.assertEqual(Point(5, 3.2) - Point(-1, -1.2), Point(6, 4.4))

    def test_mul(self):         # operator *
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)
        self.assertEqual(Point(1, 2) * Point(3, -5), -7)
        self.assertEqual(Point(7, 8) * Point(5, 6), 83)

    def test_cross(self):       # cross
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)
        self.assertEqual(Point(1, 2).cross(Point(3, -5)), -11)
        self.assertEqual(Point(7, 8).cross(Point(5, 6)), 2)
        self.assertEqual(Point(8, 7).cross(Point(6, 5)), -2)

    def test_length(self):      # length
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(6, 8).length(), 10)
        self.assertEqual(Point(6, 8).length(), 10)
        self.assertEqual(Point(5, 12).length(), 13)
        self.assertAlmostEqual(Point(1, 1).length(), sqrt(2), places=7)
        self.assertAlmostEqual(Point(1, 2).length(), 2.23606797, places=7)
        self.assertAlmostEqual(Point(3, -5).length(), 5.83095189, places=7)
        self.assertAlmostEqual(Point(5, 6).length(), 7.81024967, places=7)
        self.assertAlmostEqual(Point(6, 5).length(), 7.81024967, places=7)
        self.assertAlmostEqual(Point(7, 8).length(), 10.6301458, places=7)
        self.assertAlmostEqual(Point(8, 7).length(), 10.6301458, places=7)

    def test_hash(self):
        self.assertTrue(hash(Point(3, 4)) == hash(Point(3, 4)))
        self.assertFalse(hash(Point(3, 4)) == hash(Point(4, 3)))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
