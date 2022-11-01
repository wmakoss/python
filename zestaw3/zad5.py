#!/usr/bin/python3
# coding=utf-8

length = 12

expected_result = "|....|....|....|....|....|....|....|....|....|....|....|....|\n" \
                + "0    1    2    3    4    5    6    7    8    9   10   11   12\n"

tmp1 = (4*".").join( "|" for i in range(length+1) )+"\n"
tmp2 = "0" + "".join( str(i).rjust(5) for i in range(1,length+1))+"\n"
result = tmp1 + tmp2

print(result)

assert result == expected_result
