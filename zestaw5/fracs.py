#!/usr/bin/python3
# coding=utf-8

from math import gcd

def add_frac(frac1, frac2):        # frac1 + frac2
    result = [None, None]

    if frac1[1] < 0:
        frac1[0] *= -1
        frac1[1] *= -1

    if frac2[1] < 0:
        frac2[0] *= -1
        frac2[1] *= -1

    result[0] = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    result[1] = frac1[1] * frac2[1]

    tmp = gcd(result[0], result[1])
    result[0] /= tmp
    result[1] /= tmp

    return result

def sub_frac(frac1, frac2):        # frac1 - frac2
    result = [None, None]

    if frac1[1] < 0:
        frac1[0] *= -1
        frac1[1] *= -1

    if frac2[1] < 0:
        frac2[0] *= -1
        frac2[1] *= -1

    result[0] = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    result[1] = frac1[1] * frac2[1]

    tmp = gcd(result[0], result[1])
    result[0] /= tmp
    result[1] /= tmp

    return result

def mul_frac(frac1, frac2):        # frac1 * frac2
    result = [None, None]

    if frac1[1] < 0:
        frac1[0] *= -1
        frac1[1] *= -1

    if frac2[1] < 0:
        frac2[0] *= -1
        frac2[1] *= -1

    result[0] = frac1[0] * frac2[0]
    result[1] = frac1[1] * frac2[1]

    tmp = gcd(result[0], result[1])
    result[0] /= tmp
    result[1] /= tmp

    return result

def div_frac(frac1, frac2):        # frac1 / frac2
    return mul_frac(frac1, [frac2[1], frac2[0]])

def is_positive(frac):             # bool, czy dodatni
    if frac[1] < 0:
        frac[0] *= -1
        frac[1] *= -1
    
    if frac[0] < 0:
        return False
    else:
        return True

def is_zero(frac):                 # bool, typu [0, x]
    if frac[0] == 0 and frac[1] != 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    if frac1[1] < 0:
        frac1[0] *= -1
        frac1[1] *= -1

    if frac2[1] < 0:
        frac2[0] *= -1
        frac2[1] *= -1
    
    if frac1[0] * frac2[1] > frac2[0] * frac1[1]:
        return +1
    elif frac1[0] * frac2[1] < frac2[0] * frac1[1]:
        return -1
    else:
        return 0


def frac2float(frac):              # konwersja do float
    return float(frac[0]) / float(frac[1])

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 5], [1, 10]), [3, 10])
        self.assertEqual(add_frac([1, 5], [1, -10]), [1, 10])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 5], [1, 10]), [1, 10])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([1, 5], [1, 10]), [1, 50])

    def test_div_frac(self):
        self.assertEqual(div_frac([5, 6], [1, 2]), [5, 3])
        self.assertEqual(div_frac([5, 6], [4, -2]), [-5, 12])

    def test_is_positive(self):
        self.assertEqual(is_positive([-5, 6]), False)
        self.assertEqual(is_positive([5, -6]), False)
        self.assertEqual(is_positive([5, 6]), True)
        self.assertEqual(is_positive([0, 6]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([5, 6]), False)
        self.assertEqual(is_zero([1, 100]), False)
        self.assertEqual(is_zero([0, 6]), True)
        self.assertEqual(is_zero(self.zero), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [2, 3]), -1)
        self.assertEqual(cmp_frac([3, 6], [14, 28]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([0, 3]), 0)
        self.assertEqual(frac2float([31, 8]), 3.875)
        self.assertEqual(frac2float([-6, 2]), -3)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
