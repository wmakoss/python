#!/usr/bin/python3
# coding=utf-8

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


#tests

tests = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

expected_results = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

for i in range(len(tests)):
    result = factorial(tests[i])
    print("Test " + str(i) + ":   " + str(tests[i]) + "! = " + str(result))
    assert result == expected_results[i]
