#!/usr/bin/python3
# coding=utf-8

import random

class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):     # wstawia element w czasie O(1)
        self.items.append(item)

    def remove(self):           # zwraca losowy element w czasie O(1)
        if self.is_empty():
            raise Exception("RandomQueue is empty")
        
        rand = random.randint(0, len(self.items)-1)

        if rand != len(self.items)-1:
            # zamiana wylosowanego elementu z ostatnim
            self.items[rand], self.items[len(self.items)-1] = self.items[len(self.items)-1], self.items[rand]
        
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return False

    def clear(self):            # czyszczenie listy
        self.items.clear()


#Test
if __name__ == "__main__":

    randomqueue = RandomQueue()

    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    output = []

    for i in input:
        randomqueue.insert(i)
    
    while not randomqueue.is_empty():
        output.append(randomqueue.remove())

    print(output)
