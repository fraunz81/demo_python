#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  re_html.py
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


import re

def readFile(filename):
	'''Einlesen der Datei
	Der Inhalt wird zurückgeliefert'''
	f = open(filename, "r")
	content = f.read()
	f.close()
	return content
	

def extractLinks(website, rePat):
	'''Der übergebene Inhalt wird mit dem gegebenen Pattern überprüft.
	Das Ergebnis wird anhand eines Iterators zurückgegeben'''
	it = re.finditer(rePat, website, re.I)
	return it


def printLinks(it):
	'''Für die Darstellung der Übereinstimmungen wird der übergebene Iterator durchlaufen
	und mittels Print ausgegeben'''
	for m in it:
		print("Name: {0}, Link: {1}".format(m.group(2), m.group(1)))


p = r"<[a].*href=[\"\'](.*?)[\"\'].*>(.*?)</[a]>"
website = readFile("website01.html")
it = extractLinks(website, p)
printLinks(it)


