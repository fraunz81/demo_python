#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  decorator01.py
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


class CacheDecorator:
	def __init__(self):
		self.cache = {}
		self.func = None
	
	
	def cachedFunc(self, *args):
		if args not in self.cache:
			print("Ergebnis berechnet")
			self.cache[args] = self.func(*args)
		
		return self.cache[args]


	def __call__(self, func):
		self.func = func
		return self.cachedFunc



@CacheDecorator()
def fak(n):
	ergebnis = 1
	for i in range(2, n+1):
		ergebnis *= i

	return ergebnis


print(fak(10))
print(fak(20))
print(fak(10))
print(fak(20))
