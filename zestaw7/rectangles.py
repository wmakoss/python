#!/usr/bin/python3
# coding=utf-8

from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):        # obsługa rect1 == rect2
        if not isinstance(other, Rectangle):
            raise ValueError

        return (self.pt1, self.pt2) == (other.pt1, other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        if not isinstance(other, Rectangle):
            raise ValueError

        return not self == other

    def center(self):               # zwraca środek prostokąta
        return Point(((self.pt1.x + self.pt2.x) / 2), ((self.pt1.y + self.pt2.y) / 2))

    def area(self):                 # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)
    
    def intersection(self, other):  # część wspólna prostokątów
        if not isinstance(other, Rectangle):
            raise ValueError

        x_lower = max(self.pt1.x, other.pt1.x)
        y_lower = max(self.pt1.y, other.pt1.y)
        x_higher = min(self.pt2.x, other.pt2.x)
        y_higher = min(self.pt2.y, other.pt2.y)
        
        if x_lower >= x_higher or y_lower >= y_higher:
            return None
        else:
            return Rectangle(x_lower, y_lower, x_higher, y_higher)
        
    def cover(self, other):         # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise ValueError

        x_lower = min(self.pt1.x, other.pt1.x)
        y_lower = min(self.pt1.y, other.pt1.y)
        x_higher = max(self.pt2.x, other.pt2.x)
        y_higher = max(self.pt2.y, other.pt2.y)
        
        return Rectangle(x_lower, y_lower, x_higher, y_higher)
    
    def make4(self):                # zwraca krotkę czterech mniejszych
        upper_left = Rectangle(self.pt1.x, (self.pt1.y+self.pt2.y)/2, (self.pt1.x+self.pt2.x)/2, self.pt2.y)
        upper_right = Rectangle((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2, self.pt2.x, self.pt2.y)
        bottom_left = Rectangle(self.pt1.x, self.pt1.y, (self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)
        bottom_right = Rectangle((self.pt1.x+self.pt2.x)/2, self.pt1.y, self.pt2.x, (self.pt1.y+self.pt2.y)/2)

        return (upper_left, upper_right, bottom_left, bottom_right)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    
    def setUp(self): pass

    def test_ValueError(self):       # test ValueError
        self.assertRaises(ValueError, Rectangle, 4,-5,-3,30)
        self.assertRaises(ValueError, Rectangle, 100,100,-100,-100)

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(Rectangle(-3,-5,4,30)), "[(-3, -5), (4, 30)]")
        self.assertEqual(str(Rectangle(1,-40,5,30)), "[(1, -40), (5, 30)]")
        self.assertEqual(str(Rectangle(-453,435,43,543)), "[(-453, 435), (43, 543)]")

        self.assertEqual(repr(Rectangle(-3,-5,4,30)), "Rectangle(-3, -5, 4, 30)")
        self.assertEqual(repr(Rectangle(1,-40,5,30)), "Rectangle(1, -40, 5, 30)")
        self.assertEqual(repr(Rectangle(-453,435,43,543)), "Rectangle(-453, 435, 43, 543)")

    def test_cmp(self):         # Trzeba sprawdzać ==, !=
        self.assertTrue(Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 4))
        self.assertFalse(Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 5))
        self.assertTrue(Rectangle(2, 2, 4, 4) != Rectangle(2, 2, 4, 5))
        self.assertFalse(Rectangle(2, 2, 4, 4) != Rectangle(2, 2, 4, 4))
        self.assertTrue(Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 4))
        self.assertRaises(ValueError, Rectangle(0,0,100,100).__eq__, 100)
        self.assertRaises(ValueError, Rectangle(0,0,100,100).__eq__, "100")
        self.assertRaises(ValueError, Rectangle(0,0,100,100).__ne__, 100)
        self.assertRaises(ValueError, Rectangle(0,0,100,100).__ne__, "100")
    
    def test_center(self):
        self.assertEqual((Rectangle(-3,-5,4,30).center()), Point(0.5, 12.5))
        self.assertEqual((Rectangle(2, 2, 4, 4).center()), Point(3, 3))
        self.assertEqual((Rectangle(-100, -100, 100, 100).center()), Point(0, 0))
        self.assertEqual((Rectangle(-30, -30, -15, -5).center()), Point(-22.5, -17.5))

    def test_area(self):
        self.assertEqual((Rectangle(-3,-5,4,30).area()), 245)
        self.assertEqual((Rectangle(2, 2, 4, 4).area()), 4)
        self.assertEqual((Rectangle(-100, -100, 100, 100).area()), 40000)
        self.assertEqual((Rectangle(-30, -30, -15, -5).area()), 375)

    def test_move(self):
        self.assertEqual((Rectangle(-3,-5,4,30).move(0, 0)), Rectangle(-3,-5,4,30))
        self.assertEqual((Rectangle(2, 2, 4, 4).move(10, -15)), Rectangle(12, -13, 14, -11))
        self.assertEqual((Rectangle(-100, -100, 100, 100).move(100, 100)), Rectangle(0, 0, 200, 200))
        self.assertEqual((Rectangle(-30, -30, -15, -5).move(-.1, -.1)), Rectangle(-30.1, -30.1, -15.1, -5.1))

    def test_intersection(self):
        self.assertEqual((Rectangle(0,0,100,100).intersection(Rectangle(50,50,150,150))), Rectangle(50,50,100,100))
        self.assertEqual((Rectangle(0,0,100,100).intersection(Rectangle(150,150,250,250))), None)
        self.assertEqual((Rectangle(0,0,100,100).intersection(Rectangle(5,50,150,75))), Rectangle(5, 50, 100, 75))
        self.assertRaises(ValueError, Rectangle(0,0,100,100).intersection, 100)
        self.assertRaises(ValueError, Rectangle(0,0,100,100).intersection, "100")

    def test_cover(self):
        self.assertEqual((Rectangle(0,0,100,100).cover(Rectangle(50,50,150,150))), Rectangle(0, 0, 150, 150))
        self.assertEqual((Rectangle(0,0,100,100).cover(Rectangle(150,150,250,250))), Rectangle(0, 0, 250, 250))
        self.assertEqual((Rectangle(0,0,100,100).cover(Rectangle(5,50,150,75))), Rectangle(0, 0, 150, 100))
        self.assertRaises(ValueError, Rectangle(0,0,100,100).intersection, 100)
        self.assertRaises(ValueError, Rectangle(0,0,100,100).intersection, "100")

    def test_make4(self):
        self.assertEqual((Rectangle(0,0,100,100).make4()), (Rectangle(0, 50, 50, 100) ,Rectangle(50, 50, 100, 100) ,Rectangle(0, 0, 50, 50) ,Rectangle(50, 0, 100, 50)))
        self.assertEqual((Rectangle(0,0,1,1).make4()), (Rectangle(0, .5, .5, 1) ,Rectangle(.5, .5, 1, 1) ,Rectangle(0, 0, .5, .5) ,Rectangle(.5, 0, 1, .5)))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
