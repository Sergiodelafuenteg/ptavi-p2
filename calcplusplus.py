#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

with open(sys.argv[1]) as file_calc:

    lines = csv.reader(file_calc)

    for line in lines:
        operador = line[0]
        resultado = int(line[1])
        for arg in line[2:]:
            if operador == 'suma':
                resultado = calcoohija.CalculadoraHija(int(arg), resultado).suma()
            if operador == 'resta':
                resultado = calcoohija.CalculadoraHija(resultado, int(arg)).resta()
            if operador == 'multiplica':
                resultado = calcoohija.CalculadoraHija(int(arg), resultado).multiplica()
            if operador == 'divide':
                resultado = calcoohija.CalculadoraHija(resultado, int(arg)).divide()
        print(resultado)
