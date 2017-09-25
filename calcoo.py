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

if __init__ == "__main__":

    try:
        objeto = Calculadora("simple")
        Calculadora.init(sys.argv(1), sys.argv(3))
        print ("jajajaja")
    except ValueError:
        sys.exit("Error: Non numerical parameters")
