#!/usr/bin/python
# coding=utf-8

line = "fdsf dsfsdf\tgfsgfdg\nsdfsdf"

expected_result = 23

result = sum([ len(i) for i in line.split() ])

print(result)

assert result == expected_result
