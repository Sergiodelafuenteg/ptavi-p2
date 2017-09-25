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
    def sum(self):
        """add values"""
        return self.value1 + self.value2

    def minus(self):
        """substract values"""
        return self.value1 - self.value2

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Usalo asi: python3 ca.py operando 1 operador operando 2")

    try:
        value1 = int(sys.argv[1])
        value2 = int(sys.argv[3])
        operador = sys.argv[2]
        calculadorabasic = Calculadora(value1, value2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if operador == 'sum':
        resultado = calculadorabasic.sum()
    elif operador == 'rest':
        resultado = calculadorabasic.minus()
    else:
        sys.exit("Error: Only sum(add) or rest(substract)")

    print (resultado)
