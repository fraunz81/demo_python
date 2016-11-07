#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  taschenrechner02.py
#  
#  Copyright 2015 Franz Habison <habison.franz@gmx.at>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from argparse import ArgumentParser

parser = ArgumentParser(description = "Ein Taschenrechner")
parser.add_argument("-o", "--operation", dest = "operation", default = "plus", help = "Rechenoperation")
parser.add_argument("Operanden", metavar = "Operand", type = float, nargs = "+", help = "Operanden")
parser.add_argument("-i", "--integer", dest = "type", action = "store_const", const = int, default = float, help = "Ganzahlige Berechnung")

args = parser.parse_args()

calc = {
	"plus"	: lambda a, b: a + b,
	"minus"	: lambda a, b: a - b,
	"mal"		: lambda a, b: a * b,
	"div"		: lambda a, b: a / b
}

op = args.operation
if op in calc:
	res = 0 if op in ("plus", "minus") else 1
	for z in args.operanden:
		res = calc[op](args.op1, args.op2)
		print("Ergebnis: {}".format(res))
else:
	parser.error("{} ist keine Operation".format(op))










