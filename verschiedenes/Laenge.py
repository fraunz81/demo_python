#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Laenge.py
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


class Laenge:
	Umrechnung = {"m" : 1, "dm" : 0.1, "cm" : 0.01,
						"mm" : 0.001, "km" : 1000,
						"ft" : 0.3048,		# Fuß
						"in" : 0.0254,		# Zoll
						"mi" : 1609344		# Meilen
						}
	
	def __init__(self, zahlenwert, einheit):
		self.Zahlenwert = zahlenwert
		self.Einheit = einheit
	
	def __str__(self):
		return "{0:f}{1}".format(self.Zahlenwert, self.Einheit)
	
	def __add__(self, other):
		z = self.Zahlenwert * Laenge.Umrechnung[self.Einheit]
		z += other.Zahlenwert * Laenge.Umrechnung[other.Einheit]
		z /= Laenge.Umrechnung[self.Einheit]
		return Laenge(z, self.Einheit)

	def __sub__(self, other):
		z = self.Zahlenwert * Laenge.Umrechnung[self.Einheit]
		z -= other.Zahlenwert * Laenge.Umrechnung[other.Einheit]
		z /= Laenge.Umrechnung[self.Einheit]
		return Laenge(z, self.Einheit)



a1 = Laenge(5, "cm")
a2 = Laenge(3, "dm")
print(a1 + a2)
