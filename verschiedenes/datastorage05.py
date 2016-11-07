#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  datastorage05.py
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



import xml.sax as sax


class DictHandler(sax.handler.ContentHandler):
	
	def __init__(self):
		self.ergebnis = {}
		self.schluessel = ""
		self.wert = ""
		self.aktiv = None
		self.typ = None
	
	def startElement(self, name, attrs):
		if name == "eintrag":
			self.schluessel = ""
			self.wert = ""
		elif name == "schluessel" or name == "wert":
			self.aktiv = name
			self.typ = eval(attrs["typ"])
	
	def endElement(self, name):
		if name == "eintrag":
			self.ergebnis[self.schluessel] = self.typ(self.wert)
		elif name == "schluessel" or name == "wert":
			self.aktiv = None
	
	def characters(self, content):
		if self.aktiv == "schluessel":
			self.schluessel += content
		elif self.aktiv == "wert":
			self.wert += content


def lade_dict(dateiname):
	handler = DictHandler()
	parser = sax.make_parser()
	parser.setContentHandler(handler)
	parser.parse(dateiname)
	return handler.ergebnis

print(lade_dict("testxml.xml"))
