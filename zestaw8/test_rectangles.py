#!/usr/bin/python3
# coding=utf-8

from points import Point
from rectangles import Rectangle

import pytest

def test_print():       # test str() i repr()
    assert str(Rectangle(-3,-5,4,30)) == "[(-3, -5), (4, 30)]"
    assert str(Rectangle(1,-40,5,30)) == "[(1, -40), (5, 30)]"
    assert str(Rectangle(-453,435,43,543)) == "[(-453, 435), (43, 543)]"

    assert repr(Rectangle(-3,-5,4,30)) == "Rectangle(-3, -5, 4, 30)"
    assert repr(Rectangle(1,-40,5,30)) == "Rectangle(1, -40, 5, 30)"
    assert repr(Rectangle(-453,435,43,543)) == "Rectangle(-453, 435, 43, 543)"

def test_cmp():         # Trzeba sprawdzać ==, !=
    assert Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 4)
    assert not Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 5)
    assert Rectangle(2, 2, 4, 4) != Rectangle(2, 2, 4, 5)
    assert not Rectangle(2, 2, 4, 4) != Rectangle(2, 2, 4, 4)
    assert Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 4)

def test_center():
    assert Rectangle(-3,-5,4,30).center == Point(0.5, 12.5)
    assert Rectangle(2, 2, 4, 4).center == Point(3, 3)
    assert Rectangle(-100, -100, 100, 100).center == Point(0, 0)
    assert Rectangle(-30, -30, -15, -5).center == Point(-22.5, -17.5)

def test_area():
    assert Rectangle(-3,-5,4,30).area() == 245
    assert Rectangle(2, 2, 4, 4).area() == 4
    assert Rectangle(-100, -100, 100, 100).area() == 40000
    assert Rectangle(-30, -30, -15, -5).area() == 375

def test_move():
    assert Rectangle(-3,-5,4,30).move(0, 0) == Rectangle(-3,-5,4,30)
    assert Rectangle(2, 2, 4, 4).move(10, -15) == Rectangle(12, -13, 14, -11)
    assert Rectangle(-100, -100, 100, 100).move(100, 100) == Rectangle(0, 0, 200, 200)
    assert Rectangle(-30, -30, -15, -5).move(-.1, -.1) == Rectangle(-30.1, -30.1, -15.1, -5.1)

def test_intersection():
    assert Rectangle(0,0,100,100).intersection(Rectangle(50,50,150,150)) == Rectangle(50,50,100,100)
    assert Rectangle(0,0,100,100).intersection(Rectangle(150,150,250,250)) == None
    assert Rectangle(0,0,100,100).intersection(Rectangle(5,50,150,75)) == Rectangle(5, 50, 100, 75)

def test_cover():
    assert Rectangle(0,0,100,100).cover(Rectangle(50,50,150,150)) == Rectangle(0, 0, 150, 150)
    assert Rectangle(0,0,100,100).cover(Rectangle(150,150,250,250)) == Rectangle(0, 0, 250, 250)
    assert Rectangle(0,0,100,100).cover(Rectangle(5,50,150,75)) == Rectangle(0, 0, 150, 100)

def test_make4():
    assert Rectangle(0,0,100,100).make4() == (Rectangle(0, 50, 50, 100) ,Rectangle(50, 50, 100, 100) ,Rectangle(0, 0, 50, 50) ,Rectangle(50, 0, 100, 50))
    assert Rectangle(0,0,1,1).make4() == (Rectangle(0, .5, .5, 1) ,Rectangle(.5, .5, 1, 1) ,Rectangle(0, 0, .5, .5) ,Rectangle(.5, 0, 1, .5))

def test_from_points():
    assert Rectangle.from_points((Point(-3, -5), Point(4, 30))) == Rectangle(-3, -5, 4, 30)
    assert Rectangle.from_points((Point(2, 2), Point(4, 4))) == Rectangle(2, 2, 4, 4)
    assert Rectangle.from_points((Point(-100, -100), Point(100, 100))) == Rectangle(-100, -100, 100, 100)
    assert Rectangle.from_points((Point(-30, -30), Point(-15, -5))) == Rectangle(-30, -30, -15, -5)
    assert Rectangle.from_points((Point(-4, -5), Point(104, 105))) == Rectangle(-4, -5, 104, 105)

def test_top_left_bottom_right():
    tmp = Rectangle(2, 1, 4, 3)
    assert tmp.top == 3
    assert tmp.left == 2
    assert tmp.bottom == 1
    assert tmp.right == 4
    tmp.top = 100
    tmp.right = 75
    tmp.left = 50
    tmp.bottom = -10
    assert tmp.top == 100
    assert tmp.left == 50
    assert tmp.bottom == -10
    assert tmp.right == 75

def test_width_height():
    tmp = Rectangle(1, 2, 4, 3)
    assert tmp.height == 1
    assert tmp.width == 3
    tmp.height = 50
    tmp.width = 100
    assert tmp.height == 50
    assert tmp.width == 100
    assert str(tmp) == "[(1, 2), (101, 52)]"

def test_topleft_bottomleft_topright_bottomright():
    tmp = Rectangle(50, 50, 51, 51)
    tmp.topleft = Point(25, 75)
    tmp.bottomright = Point(70, 30)
    assert str(tmp) == "[(25, 30), (70, 75)]"
    tmp.bottomleft = Point(5, 0)
    tmp.topright = Point(100, 105)
    assert str(tmp) == "[(5, 0), (100, 105)]"
    assert tmp.topleft == Point(5, 105)
    assert tmp.bottomleft == Point(5, 0)
    assert tmp.topright == Point(100, 105)
    assert tmp.bottomright == Point(100, 0)


if __name__ == "__main__":
    pytest.main()
