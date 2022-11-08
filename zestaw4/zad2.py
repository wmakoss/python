#!/usr/bin/python3
# coding=utf-8

def make_ruler(n):
    tmp1 = (4*".").join( "|" for i in range(n+1) )+"\n"
    tmp2 = "0" + "".join( str(i).rjust(5) for i in range(1,n+1))+"\n"
    result = tmp1 + tmp2
    return result

def make_grid(rows, cols):
    tmp1 = (3*" ").join("|" for i in range(cols+1)) + "\n" # "|   |   |   |   |\n"
    tmp2 = (3*"-").join("+" for i in range(cols+1)) + "\n" # "+---+---+---+---+\n"
    result = tmp1.join(tmp2 for i in range(rows+1))
    return result


print(make_ruler(12))

print(make_grid(2, 4))
