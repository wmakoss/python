#!/usr/bin/python3
# coding=utf-8

def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        else:
            result += item
    return result


#test

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

expected_result = 45

result = sum_seq(seq)

print(result)

assert result == expected_result
