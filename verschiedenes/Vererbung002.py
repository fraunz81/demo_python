#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Vererbung002.py
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


class A:
	def __init__(self):
		self.X = 1337
		print("Konstruktor von A")
	
	def m(self):
		print("Methode m von A, Es ist self.X = ", self.X)
	

class B(A):
	def __init__(self):
		A.__init__(self)
		self.Y = 10000
		print("Konstruktor von B")

	def n(self):
		print("Methode n von B")

b = B()
b.n()
b.m()
