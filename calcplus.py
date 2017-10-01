#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

file_calc = open(sys.argv[1])

for line in file_calc.readlines():
    args = line[:line.find(',')]

print (args)
