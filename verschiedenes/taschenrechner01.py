#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  taschenrechner01.py
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

parser = ArgumentParser()
parser.add_argument("-o", "--operation", dest="operation", default="plus")
parser.add_argument("op1", type=float)
parser.add_argument("op2", type=float)

args = parser.parse_args()

calc = {
	"plus"	: lambda a, b: a + b,
	"minus"	: lambda a, b: a - b,
	"mal"		: lambda a, b: a * b,
	"div"		: lambda a, b: a / b
}

op = args.operation
if op in calc:
	print("Ergebnis: {}".format(calc[op](args.op1, args.op2)))
else:
	parser.error("{} ist keine Operation".format(op))
