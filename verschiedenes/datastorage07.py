#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  datastorage07.py
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


import xml.etree.ElementTree as exml

def lese_text(element):
	typ = element.get("typ", "str")
	erg = "{}('{}')".format(typ, element.text)
	print(erg)
	return eval(erg)


def lade_dict(dateiname):
	d = {}
	baum = exml.parse(dateiname)
	tag_dict = baum.getroot()
	for eintrag in tag_dict:
		tag_schluessel = eintrag.find("schluessel")
		tag_wert = eintrag.find("wert")
		schluessel = lese_text(tag_schluessel)
		wert = lese_text(tag_wert)
		#print ("Schluessel: {0}; Wert: {1}".format(schluessel, wert))
		d[schluessel] = wert
	
	return d

print(lade_dict("testxml.xml"))
