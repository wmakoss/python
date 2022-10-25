#!/usr/bin/python
# coding=utf-8

line = "fdsf dsfsdf\tgfsgfdg\nsdfsdf"

expected_result_1 = "gfsgfdg"

expected_result_2 = 7

tmp = max([ [len(i),i] for i in line.split() ])

result_1 = tmp[1]

result_2 = tmp[0]

print(result_1)

print(result_2)

assert result_1 == expected_result_1

assert result_2 == expected_result_2
