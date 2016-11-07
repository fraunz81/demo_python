#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Iteratoren.py
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


class Fibonacci:
	def __init__(self, max_n):
		self.MaxN = max_n
		self.N = 0
		self.A = 0
		self.B = 0
	
	def __iter__(self):
		self.N = 0
		self.A = 0
		self.B = 1
		return self
	
	def __next__(self):
		if self.N < self.MaxN:
			self.N += 1
			self.A, self.B = self.B, self.A + self.B
			return self.A
		else:
			raise StopIteration


class GoldenerSchnitt(Fibonacci):
	def __next__(self):
		Fibonacci.__next__(self)
		return self.B / self.A


class Fibonacci2:
	def __init__(self, max_n):
		self.MaxN = max_n
	
	def __iter__(self):
		n = 0
		a, b = 0, 1
		for n in range(self.MaxN):
			a, b = b, a + b
			yield a


class Fibonacci3:
	class FibnoacciIterator:
		def __init__(self, max_n):
			self.MaxN = max_n
			self.N, self.A, self.B = 0, 0, 1
		
		def __iter__(self):
			return self
		
		def __next__(self):
			if self.N < self.MaxN:
				self.N += 1
				self.A, self.B = self.B, self.A + self.B
				return self.A
			else:
				raise StopIteration
	
	def __init__(self, max_n):
		self.MaxN = max_n
	
	def __iter__(self):
		return self.FibnoacciIterator(self.MaxN)




for f in Fibonacci(14):
	print(f, end = " ")

print()
print(list(Fibonacci(16)))
print(sum(Fibonacci(60)))

l = Fibonacci(3)
for i in l:
	for j in l:
		print(i, j, end = ", ")
		
	print()


for g in GoldenerSchnitt(14):
	print("{0:.6f}".format(g), end = " ")


print()
print()
print("Finboacci2 Tests")
print()
# Fibonacci2
print(list(Fibonacci2(10)))

l = Fibonacci2(3)
for i in l:
	for j in l:
		print(i, j, end = ", ")
		
	print()


print()
print()
print("Finboacci3 Tests")
print()
# Fibonacci3
print(list(Fibonacci3(10)))

l = Fibonacci3(3)
for i in l:
	for j in l:
		print(i, j, end = ", ")
		
	print()

