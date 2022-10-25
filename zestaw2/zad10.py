#!/usr/bin/python
# coding=utf-8

line = "fdsf dsfsdf\tgfsgfdg\nsdfsdf"

expected_result = 4

result = len( line.split() )

print(result)

assert result == expected_result
