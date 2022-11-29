#!/usr/bin/python3
# coding=utf-8

# Stworzyć następujące iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,

class Generator01:

    def __init__(self, first_value = 0):
        self.value = first_value

    def __iter__(self):
        return self

    def __next__(self):
        result = self.value
        self.value = (self.value + 1) % 2
        return result

    next = __next__

iterator_a = iter(Generator01())

# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],

import random

iterator_b = (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))

# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].

import itertools

iterator_c = itertools.cycle(range(7))

# Test

if __name__ == "__main__":

    print("iterator_a:")
    for i in range(20):
        print(next(iterator_a), end=" ")
    print("")

    print("iterator_b:")
    for i in range(20):
        print(next(iterator_b), end=" ")
    print("")

    print("iterator_c:")
    for i in range(20):
        print(next(iterator_c), end=" ")
    print("")
