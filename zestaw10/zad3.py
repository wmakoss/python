#!/usr/bin/python3
# coding=utf-8

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # tablica elementow
        self.exist = size * [False]
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise Exception("Stack is full")
        if not self.exist[data]:
            self.items[self.n] = data
            self.n += 1
            self.exist[data] = True

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        self.exist[data] = False
        return data


#Test
if __name__ == "__main__":
    
    stack = Stack(100)

    input = [1, 3, 8, 34, 24, 6, 76, 34, 4, 23, 1]
    expected_output = [23, 4, 76, 6, 24, 34, 8, 3, 1]
    output = []

    for i in input:
        stack.push(i)
    
    while not stack.is_empty():
        output.append(stack.pop())

    print(output)

    assert output == expected_output
