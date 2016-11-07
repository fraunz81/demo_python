#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2014 Franz Habison <habison.franz@gmx.at>
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

import factorial
import kehrwert
import sortierteListe


zahl = 1
while zahl > 0:
	zahl = int(input("Geben Sie eine ganze Zahl ein: "))
	if zahl > 0:
		print("Fakultät: ", factorial.factorial(zahl))
		print("Kehrwert: ", kehrwert.kehr(zahl))

# Test mit der Klasse sortierteListe
l = sortierteListe.SortierteListe([6, 4, 3])
print(l)
l.append(2)
print(l)
l.extend([67, 0, -56])
print(l)
l += [100, 5]
print(l)
l *= 2
print(l)
