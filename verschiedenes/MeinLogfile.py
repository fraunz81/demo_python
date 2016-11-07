#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MeinLogfile.py
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


'''Eine Klasse für rudimentäre Logeinträge'''

class MeinLogfile:
	def __init__(self, logfile):
		self.logfile = logfile
		self.f = None
	
	def eintrag(self, text):
		self.f.write("==>{0}\n".format(text))
	
	def __enter__(self):
		self.f = open(self.logfile, "w")
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		self.f.close()


with MeinLogfile("logfile.txt") as log:
	log.eintrag("Hallo Welt")
	log.eintrag("Was geht?")
