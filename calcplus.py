#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

file_calc = open(sys.argv[1], 'r')

args = file_calc.readlines()

"""evito saltos de linea"""

#args = args.remove('\n')
print (args)

for i in args:
    i.rstrip(['\n'])

print (args[0])
