#!/usr/bin/python
# coding=utf-8

line = "fdsf dsfsdf\tgfsgfdg\nsdfsdf"

expected_result_1 = "fdgs"

expected_result_2 = "ffgf"

result_1 = "".join([ i[0] for i in line.split() ])

result_2 = "".join([ i[ len(i)-1 ] for i in line.split() ])

print(result_1)

print(result_2)

assert result_1 == expected_result_1

assert result_2 == expected_result_2
