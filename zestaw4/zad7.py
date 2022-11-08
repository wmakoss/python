#!/usr/bin/python3
# coding=utf-8

def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            if any(isinstance(item2, (list, tuple)) for item2 in item):
                item = flatten(item)
            for item2 in item:
                result.append(item2)
        else:
            result.append(item)
    return result


#test

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = flatten(seq)

print(result)

assert result == expected_result
