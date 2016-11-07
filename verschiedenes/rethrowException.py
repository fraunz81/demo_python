#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rethrowException.py
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


def function3():
	raise TypeError

def function2():
	function3()

def function1():
	try:
		function2()
	except TypeError:
		#Fehlerbehandlung
		raise TypeError

try:
	function1()
except:
	print("Ende 1")


# Die "richtige" Art eine Exception nochmals zu werfen
print("")
print("Die richtige Art")
print("")

def function6():
	raise TypeError

def function5():
	function6()

def function4():
	try:
		function5()
	except TypeError as e:
		#Fehlerbehandlung
		raise

function4()

