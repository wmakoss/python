#!/usr/bin/python
# coding=utf-8

liczba = 304702937409285094850938405983405209758247583745837040

expected_result = 10

result = str(liczba).count("0")

print(result)

assert result == expected_result
