#!/usr/bin/python
# coding=utf-8

L = [123, 456, 34, 7, 76, 3, 36, 234]

expected_result = "123, 456, 034, 007, 076, 003, 036, 234"

result = ", ".join( [ str(i).zfill(3) for i in L ] )

print(result)

assert result == expected_result
