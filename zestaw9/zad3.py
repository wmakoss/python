#!/usr/bin/python3
# coding=utf-8

class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0   # może to trzymać w polu data wartownika?
        self.nil = Node()   # wartownik
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def is_empty(self):
        # return self.length == 0
        return self.nil.next == self.nil

    def count(self):
        return self.length

    def insert_head(self, node):
        node.next = self.nil.next
        node.prev = self.nil
        self.nil.next.prev = node
        self.nil.next = node
        self.length += 1

    def insert_tail(self, node):
        node.next = self.nil
        node.prev = self.nil.prev
        self.nil.prev.next = node
        self.nil.prev = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.nil.next
        # Teraz ogólny schemat usuwania węzła.
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None   # czyszczenie
        self.length -= 1
        return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.nil.prev
        # Teraz ogólny schemat usuwania węzła.
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None   # czyszczenie
        self.length -= 1
        return node

    def find_max(self): # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        node = self.nil.next
        max = node.data
        maxnode = node
        while node != self.nil:
            if node.data > max:
                max = node.data
                maxnode = node
            node = node.next
        return maxnode

    def find_min(self): # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        node = self.nil.next
        min = node.data
        minnode = node
        while node != self.nil:
            if node.data < min:
                min = node.data
                minnode = node
            node = node.next
        return minnode

    def remove(self, node): # Usuwa wskazany węzeł z listy (węzeł należy do listy).
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None   # czyszczenie
        self.length -= 1
        return node

    def clear(self): # czyszczenie listy
        # opcjonalne usuwanie wszystkich połączeń
        node = self.nil.next
        while node != self.nil:
            tmp = node.next
            node.next = None
            node.prev = None
            node = tmp
        # czyszczenie listy
        self.nil.next = self.nil
        self.nil.prev = self.nil
        self.length = 0

# Testy

if __name__ == "__main__":

    mylist = DoubleList()
    mylist.insert_tail(Node(11))
    mylist.insert_tail(Node(22))
    tmp = Node(33)
    mylist.insert_head(tmp)
    mylist.insert_head(Node(10))

    print(f"Min: {mylist.find_min()}")
    print(f"Min: {mylist.find_max()}")
    print(f"Length: {mylist.length}")
    print(f"is empty: {mylist.is_empty()}")
    print("")
    
    mylist.remove(tmp)
    
    print(f"Min: {mylist.find_min()}")
    print(f"Min: {mylist.find_max()}")
    print(f"Length: {mylist.length}")
    print(f"is empty: {mylist.is_empty()}")
    print("")
    
    mylist.clear()

    print(f"Min: {mylist.find_min()}")
    print(f"Min: {mylist.find_max()}")
    print(f"Length: {mylist.length}")
    print(f"is empty: {mylist.is_empty()}")
    print("")
