#!/usr/bin/python3
# coding=utf-8

x = [1, 2, "a", "b", 3, 4]
y = [2, 4, "b", "c", 6, 8]

expected_result1 = {2, 4, 'b'}
expected_result2 = {1, 2, 3, 4, 6, 8, 'a', 'b', 'c'}

result1 = set(x).intersection(set(y))
result2 = set(x).union(set(y))

print(result1)
print(result2)

assert result1 == expected_result1
assert result2 == expected_result2
