#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  interpreter01.py
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

# In der Konsole dann die Funktion eingeben
# z.B: def f(x): return pi * r**2


print("Definieren Sie eine Funktion f mit einem Parameter:")
definition = input()
kontext = {"pi" : 3.1459}
exec(definition, kontext)
#print(kontext)
for i in range(5):
	print("f({0}) = {1}".format(i, kontext['f'](i)))
