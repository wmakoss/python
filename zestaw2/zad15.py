#!/usr/bin/python
# coding=utf-8

L = [123 , 456, 789]

expected_result = "123456789"

result = "".join([ str(i) for i in L ])

print(result)

assert result == expected_result
