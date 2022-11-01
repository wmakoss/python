#!/usr/bin/python3
# coding=utf-8


L = [3, 5, 4] ; L = L.sort()
# Metoda .sort() sortuje objekt na którym została wywołana więc wystarczy L.sort()


x, y = 1, 2, 3
# W powyższym przypisaniu jest inna ilość elementów po lewej i po prawej stronie


X = 1, 2, 3 ; X[1] = 4
# Po powyższym przypisaniu (X = 1, 2, 3) X jest krotką, a krotka nie może zmieniać swoich wartości
# więc zmiana wartości X[1] = 4 jest niepoprawna


X = [1, 2, 3] ; X[3] = 4
# Powyższa lista X jest 3 elementowa wiec posiada wartosci na indexach 0, 1 i 2 więc index 3 nie istnieje


X = "abc" ; X.append("d")
# X jest stringiem więc nie można zmieniać jego wartości (można stworzyć nowy string X = X + "d")


L = list(map(pow, range(8)))
# funkcja pow wymaga co najmniej 2 argumentów a range(8) to lista która zawiera pojedyncze elementy
