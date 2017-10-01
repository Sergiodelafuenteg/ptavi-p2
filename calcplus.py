#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

file_calc = open(sys.argv[1], 'r')

args = file_calc.read()
args = args.split(',')
print (args)
print (args[0])
