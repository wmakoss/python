#!/usr/bin/python3
# coding=utf-8

while True:
    x = input()
    if x == "stop":
        break
    else:
        try:
            print(str(float(x)) + " " + str(float(x)**3))
        except:
            print("Error: Wprowadzona wartość nie jest liczbą. Proszę podać liczbę.")
