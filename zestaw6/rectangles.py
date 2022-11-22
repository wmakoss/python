#!/usr/bin/python3
# coding=utf-8

from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def fixPointsOrder(self):
        minx = min(self.pt1.x, self.pt2.x)
        miny = min(self.pt1.y, self.pt2.y)
        maxx = max(self.pt1.x, self.pt2.x)
        maxy = max(self.pt1.y, self.pt2.y)
        self.pt1 = Point(minx, miny)
        self.pt2 = Point(maxx, maxy)


    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.fixPointsOrder()

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        self.fixPointsOrder()
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        self.fixPointsOrder()
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):        # obsługa rect1 == rect2
        self.fixPointsOrder()
        other.fixPointsOrder()
        return (self.pt1, self.pt2) == (other.pt1, other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta
        self.fixPointsOrder()
        return Point(((self.pt1.x + self.pt2.x) / 2), ((self.pt1.y + self.pt2.y) / 2))

    def area(self):                 # pole powierzchni
        self.fixPointsOrder()
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        self.fixPointsOrder()
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    
    def setUp(self): pass

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(Rectangle(4,-5,-3,30)), "[(-3, -5), (4, 30)]")
        self.assertEqual(str(Rectangle(1,30,5,-40)), "[(1, -40), (5, 30)]")
        self.assertEqual(str(Rectangle(43,435,-453,543)), "[(-453, 435), (43, 543)]")

        self.assertEqual(repr(Rectangle(4,-5,-3,30)), "Rectangle(-3, -5, 4, 30)")
        self.assertEqual(repr(Rectangle(1,30,5,-40)), "Rectangle(1, -40, 5, 30)")
        self.assertEqual(repr(Rectangle(43,435,-453,543)), "Rectangle(-453, 435, 43, 543)")

    def test_cmp(self):         # Trzeba sprawdzać ==, !=
        self.assertTrue(Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 4))
        self.assertFalse(Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 5))
        self.assertTrue(Rectangle(2, 2, 4, 4) != Rectangle(2, 2, 4, 5))
        self.assertFalse(Rectangle(2, 2, 4, 4) != Rectangle(2, 2, 4, 4))
        self.assertTrue(Rectangle(4, 2, 2, 4) == Rectangle(4, 4, 2, 2))
    
    def test_center(self):
        self.assertEqual((Rectangle(4,-5,-3,30).center()), Point(0.5, 12.5))
        self.assertEqual((Rectangle(4, 2, 2, 4).center()), Point(3, 3))
        self.assertEqual((Rectangle(100, 100, -100, -100).center()), Point(0, 0))
        self.assertEqual((Rectangle(-30, -30, -15, -5).center()), Point(-22.5, -17.5))

    def test_area(self):
        self.assertEqual((Rectangle(4,-5,-3,30).area()), 245)
        self.assertEqual((Rectangle(4, 2, 2, 4).area()), 4)
        self.assertEqual((Rectangle(100, 100, -100, -100).area()), 40000)
        self.assertEqual((Rectangle(-30, -30, -15, -5).area()), 375)

    def test_move(self):
        self.assertEqual((Rectangle(4,-5,-3,30).move(0, 0)), Rectangle(4,-5,-3,30))
        self.assertEqual((Rectangle(4, 2, 2, 4).move(10, -15)), Rectangle(12, -13, 14, -11))
        self.assertEqual((Rectangle(100, 100, -100, -100).move(100, 100)), Rectangle(0, 0, 200, 200))
        self.assertEqual((Rectangle(-30, -30, -15, -5).move(-.1, -.1)), Rectangle(-30.1, -30.1, -15.1, -5.1))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
