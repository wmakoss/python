#!/usr/bin/python3
# coding=utf-8

x = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

expected_result = [0, 4, 3, 7, 18]

result = [sum(i) for i in x]

print(result)

assert result == expected_result
