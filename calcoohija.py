#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora:
    """class for sum and substract."""

    def __init__(self, value1, value2):
        """initialize selfs"""
        self.value1 = value1
        self.value2 = value2
    def sum(self):
        """add values"""
        return self.value1 + self.value2

    def minus(self):
        """substract values"""
        return self.value1 - self.value2

class CalculadoraHija(Calculadora):
    """Class for multiply and divide"""
    def __init__(self, value1, value2):
        """initialize selfs"""
        Calculadora.__init__(self, value1, value2)
        """Aggregate Values"""
        self.value1 = value1
        self.value2 = value2
    def sum(self):
        """multiply values"""
        return self.value1 * self.value2

    def minus(self):
        """divide values"""
        return self.value1 / self.value2


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Usalo asi: python3 calcoo.py operando 1 operador operando 2")

    try:
        value1 = int(sys.argv[1])
        value2 = int(sys.argv[3])
        operador = sys.argv[2]
        calculadora = CalculadoraHija(value1, value2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if operador == 'sum':
        resultado = calculadora.sum()
    elif operador == 'rest':
        resultado = calculadora.minus()
    elif operador == 'multi':
        resultado = calculadora.multi()
    elif operador == 'div':
        resultado = calculadora.div()
    else:
        sys.exit("Error: Only sum(add) or rest(substract)")

    print (resultado)
