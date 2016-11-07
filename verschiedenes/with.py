#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  with.py
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


f = open("datei.txt", "r")
try:
	print(f.read())
finally:
	f.close()

#oder mit with
with open("programm.py", "r") as f:
	print(f.read())

#oder mehrere with
with open("file1.txt", "r") as f1, with open("file2.txt", "r") as f2:
	print(f1.read())
	print(f2.read())

# kann auch verschachtelt geschrieben werden
with open("file.txt", "r") as f1:
	with open("file2.txt", "r") as f2:
		print(f1.read())
		print(f2.read())


