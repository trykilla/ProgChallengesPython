#!/usr/bin/python3

def insert():
    return lista.insert

def azul():
    return "azul"

def default():
    return "negro"

switcher = {
        "blanco": blanco,
        "azul": azul,
        "default": default
    }

def switch(color):
    return switcher.get(color, default)()

n = str(input())
print(switch(n))

