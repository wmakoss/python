#!/usr/bin/python
# coding=utf-8

line = "fdsf dsfsdf\tgfsgfdg\nsd_GvR_fsdf"

expected_result = "fdsf dsfsdf\tgfsgfdg\nsd_Guido van Rossum_fsdf"

result = line.replace("GvR", "Guido van Rossum")

print(result)

assert result == expected_result
