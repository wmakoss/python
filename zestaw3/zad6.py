#!/usr/bin/python3
# coding=utf-8

height = 2
width = 4

expected_result = "+---+---+---+---+\n" \
                + "|   |   |   |   |\n" \
                + "+---+---+---+---+\n" \
                + "|   |   |   |   |\n" \
                + "+---+---+---+---+\n"

tmp1 = (3*" ").join("|" for i in range(width+1)) + "\n" # "|   |   |   |   |\n"

tmp2 = (3*"-").join("+" for i in range(width+1)) + "\n" # "+---+---+---+---+\n"

result = tmp1.join(tmp2 for i in range(height+1))

print(result)

assert result == expected_result
