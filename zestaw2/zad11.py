#!/usr/bin/python
# coding=utf-8

text = "word"

expected_result = "w_o_r_d"

result = "_".join(text)

print(result)

assert result == expected_result
