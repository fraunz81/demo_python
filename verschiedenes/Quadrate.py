'''Doc zum Modul Quadrate'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Quadrate.py
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

class Quadrate:
	'''Zur Demonstration der Magic Funktion __getitem__'''
	
	def __init__(self, max_n):
		'''Konstruktor der Klasse Quadrate - initialisert die Klasse'''
		self.MaxN = max_n
	
	def __getitem__(self, index):
		index += 1 # 0 * 0 ist nicht sehr interessant
		if index > len(self) or index < 1:
			raise IndexError
		
		return index * index


	def __len__(self):
		return self.MaxN


print(__doc__)
print(Quadrate.__doc__)
print(list(Quadrate(20)))
