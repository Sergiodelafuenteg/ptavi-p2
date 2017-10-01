#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):
    """Class for multiply and divide"""
    def __init__(self, value1, value2):
        """initialize selfs"""
        calcoo.Calculadora.__init__(self, value1, value2)
        """Aggregate Values"""
        self.value1 = value1
        self.value2 = value2
    def multi(self):
        """multiply values"""
        return self.value1 * self.value2

    def divide(self):
        """divide values"""
        try:
            self.value1 / self.value2
        except ZeroDivisionError:
            sys.exit("No se dividir por cero")
        return self.value1 / self.value2


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Usalo asi: python3 calcoo.py operando 1 operador operando 2")

    try:
        value1 = float(sys.argv[1])
        value2 = float(sys.argv[3])
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
        resultado = calculadora.divide()
    else:
        sys.exit("Error: Only sum(add) or rest(substract)")

    print (resultado)
