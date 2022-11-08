#!/usr/bin/python3
# coding=utf-8

def fibonacci(n):
    result = 0
    previous = 1
    for i in range(n):
        result, previous = result + previous, result
    return result


#tests

tests = [1, 2, 3, 4, 5, 6, 7, 8, 9]

expected_results = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

for i in range(len(tests)):
    result = fibonacci(tests[i])
    print("Test " + str(i) + ":   fib(" + str(tests[i]) + ") = " + str(result))
    assert result == expected_results[i]
