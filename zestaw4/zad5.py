#!/usr/bin/python3
# coding=utf-8

def odwracanie_iteracyjne(L, left, right):
    leftindex = left
    rightindex = right
    while True:
        if leftindex < rightindex:
            L[leftindex], L[rightindex] = L[rightindex], L[leftindex]
            leftindex += 1
            rightindex -= 1
        else:
            break


def odwracanie_rekurencyjne(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjne(L, left+1, right-1)


#tests

test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
left = 3
right = 8

expected_result = [0, 1, 2, 8, 7, 6, 5, 4, 3, 9, 10]

odwracanie_iteracyjne(test, left, right)

print(test)

assert test == expected_result

test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odwracanie_rekurencyjne(test, left, right)

print(test)

assert test == expected_result
