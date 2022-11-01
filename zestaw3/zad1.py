#!/usr/bin/python3
# coding=utf-8

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# Powyższy kod jest poprawny ale 3 średniki ";" na końcach lini są niepotrzebne

for i in "axby": if ord(i) < 100: print (i)

# Powyższy kod nie jest poprawny poniewaz w 1 lini jest pętla for i instrukcja warunkowa

for i in "axby": print (ord(i) if ord(i) < 100 else i)

# Powyższy kod jest poprawny poniewaz w 1 lini jest pętla for po której jest wykonywana tylko 1 instrukcja
