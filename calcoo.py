#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora:
    """class for sum and substract."""

    def __init__(self, value1, value2):
        """initialize selfs"""
        self.value1 = value1
        self.value2 = value2
        #self.operador = operador
    def sum():

         return self.value1 + self.value2

    def minus():

         return self.value1 - self.value2

if __name__ == "__main__":

    try:
        value1 = int(sys.argv[1])
        value2 = int(sys.argv[3])
        operador = sys.argv[2]
        calculadorabasic = Calculadora(value1, value2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    print ("jajajaja")
    if operador == 'sum':
        calculadorabasic.sum()
    elif operador == 'rest':
        calculadorabasic.minus()
