#!/usr/bin/python3
# coding=utf-8

roman2intmap1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

roman2intmap2 = {}
roman2intmap2["I"] = 1
roman2intmap2["V"] = 5
roman2intmap2["X"] = 10
roman2intmap2["L"] = 50
roman2intmap2["C"] = 100
roman2intmap2["D"] = 500
roman2intmap2["M"] = 1000

assert roman2intmap1 == roman2intmap2


def roman2int(roman, roman2intmap):
    value = 0
    for i in range(len(roman)):
        if i == len(roman)-1:
            value = value + roman2intmap[roman[i]]
        elif roman2intmap[roman[i]] < roman2intmap[roman[i+1]]:
            value = value - roman2intmap[roman[i]]
        else:
            value = value + roman2intmap[roman[i]]
    return value


tests = ["XI", "IV", "VII", "XIX", "XL", "XCV", "CM", "MXXV", "MCMXCV", "MM", "MCMLVI", "MMXI", "MMMDCCCLXXXVIII", "MMXXII", "MMMMMMMMMM"]

expected_results = [11, 4, 7, 19, 40, 95, 900, 1025, 1995, 2000, 1956, 2011, 3888, 2022, 10000]

for i in range(len(tests)):
    result = roman2int(tests[i], roman2intmap1)
    print("Test " + str(i) + ": " + tests[i] + " = " + str(result))
    assert result == expected_results[i]
