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
    
    @classmethod
    def from_points(cls, sequence):   # dodatkowy konstruktor
        new_rectangle = cls(sequence[0].x, sequence[0].y, sequence[1].x, sequence[1].y)   # działa zwykły konstruktor
        return new_rectangle
    
    @property
    def top(self):
        return self.pt2.y

    @top.setter
    def top(self, value):
        if value <= self.pt1.y:
            raise ValueError
        else:
            self.pt2.y = value

    @property
    def left(self):
        return self.pt1.x

    @left.setter
    def left(self, value):
        if value >= self.pt2.x:
            raise ValueError
        else:
            self.pt1.x = value

    @property
    def bottom(self):
        return self.pt1.y

    @bottom.setter
    def bottom(self, value):
        if value >= self.pt2.y:
            raise ValueError
        else:
            self.pt1.y = value

    @property
    def right(self):
        return self.pt2.x

    @right.setter
    def right(self, value):
        if value <= self.pt1.x:
            raise ValueError
        else:
            self.pt2.x = value

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError
        else:
            self.pt2.x = self.pt1.x + value

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError
        else:
            self.pt2.y = self.pt1.y + value

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @topleft.setter
    def topleft(self, value):
        self.left = value.x
        self.top = value.y

    @property
    def bottomleft(self):
        return self.pt1

    @bottomleft.setter
    def bottomleft(self, value):
        self.left = value.x
        self.bottom = value.y

    @property
    def topright(self):
        return self.pt2

    @topright.setter
    def topright(self, value):
        self.right = value.x
        self.top = value.y

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)

    @bottomright.setter
    def bottomright(self, value):
        self.right = value.x
        self.bottom = value.y

    @property
    def center(self):
        return Point(((self.pt1.x + self.pt2.x) / 2), ((self.pt1.y + self.pt2.y) / 2))

    @center.setter
    def center(self, value):
        tmp = self.move(value.x - ((self.pt1.x + self.pt2.x) / 2), value.y - ((self.pt1.y + self.pt2.y) / 2))
        self.pt1 = tmp.pt1
        self.pt2 = tmp.pt2
