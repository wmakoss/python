#!/usr/bin/python
# coding=utf-8

line = "fdsf dsfsdf\tgfsgfdg\nsdfsdf"

expected_result_1 = ['dsfsdf', 'fdsf', 'gfsgfdg', 'sdfsdf']

expected_result_2 = ['fdsf', 'dsfsdf', 'sdfsdf', 'gfsgfdg']

result_1 = sorted(line.split())

result_2 = [ j[1] for j in sorted( [ [len(i),i] for i in line.split() ] ) ]

print(result_1)

print(result_2)

assert result_1 == expected_result_1

assert result_2 == expected_result_2
