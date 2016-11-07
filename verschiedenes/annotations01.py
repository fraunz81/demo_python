#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  annotations01.py
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


def strmult(s: str, n: int) -> str:
	return s * n


def call(f, **kwargs):
	for arg in kwargs:
		if arg not in f.__annotations__:
			raise TypeError("Parameter '{0}' unbekannt".format(arg))
		
		if not isinstance(kwargs[arg], f.__annotations__[arg]):
			raise TypeError("Parameter '{0}' hat ungültigen Typ".format(arg))
		
	ret = f(**kwargs)
	if type(ret) != f.__annotations__["return"]:
		raise TypeError("Ungültiger Rückgabewert")
	
	return ret


print(call(strmult, s="Hallo", n=3))

print(call(strmult, s="Hallo", n="Welt"))

print(call(strmult, s=87, n=37))
