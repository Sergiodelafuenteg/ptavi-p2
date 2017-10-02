#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import os

file_calc = open(sys.argv[1], 'r')

lines = file_calc.readlines()

#resultado = {}

"""evito saltos de linea"""

for line in lines:
    args = line.split(',')
    operador = args[0]
    resultado = 0
    for arg in args[1:]:

        if operador == 'suma':
            resultado = calcoohija.CalculadoraHija(int(arg),resultado).suma()
        if operador == 'resta':
            resultado = calcoohija.CalculadoraHija(int(arg),resultado).resta()
        if operador == 'multiplica':
            resultado = calcoohija.CalculadoraHija(int(arg),resultado).multiplica()
        if operador == 'divide':
            resultado = calcoohija.CalculadoraHija(int(arg),resultado).divide()

#args = args.remove('\n')

print ('resultado = %s' % (resultado))
