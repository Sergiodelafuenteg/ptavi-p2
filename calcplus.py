#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

file_calc = open(sys.argv[1], 'r')

lines = file_calc.readlines()

for line in lines:
    args = line.split(',')
    operador = args[0]
    resultado = int(args[1])
    for arg in args[2:]:
        if operador == 'suma':
            resultado = calcoohija.CalculadoraHija(int(arg),resultado).suma()
        if operador == 'resta':
            resultado = calcoohija.CalculadoraHija(resultado,int(arg)).resta()
        if operador == 'multiplica':
            resultado = calcoohija.CalculadoraHija(int(arg),resultado).multiplica()
        if operador == 'divide':
            resultado = calcoohija.CalculadoraHija(resultado,int(arg)).divide()
    print (resultado)
