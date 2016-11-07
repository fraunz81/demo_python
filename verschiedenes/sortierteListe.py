#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sortierteListe.py
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


class SortierteListe(list):
	def __init__(self, *args, **kwargs):
		list.__init__(self, *args, **kwargs)
		self.sort()
	
	def __setitem__(self, key, value):
		list.__setitem__(self, key, value)
		self.sort()
	
	def append(self, value):
		list.append(self, value)
		self.sort()
	
	def extend(self, sequence):
		list.extend(self, sequence)
		self.sort()
	
	def insert(self, i, x):
		list.insert(self, i, x)
		self.sort()
	
	def reverse(self):
		pass
	
	def __iadd__(self, s):
		erg = list.__iadd__(self, s)
		self.sort()
		return erg
	
	def __imul__(self, n):
		erg = list.__imul__(self, n)
		self.sort()
		return erg
