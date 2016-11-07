#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  datastorage02.py
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

##########################################
# Dieses Beispiel funktioniert noch nicht
##########################################

import xml.dom.minidom as dom

def knoten_auslesen(knoten):
	return eval("{}('{}')".format(knoten.getAttribute("typ"), knoten.firstChild.data.strip()))


def lade_dict(dateiname):
	d = {}
	with dom.parse(dateiname) as baum:
		if baum.firstChild.nodeName != "dictionary":
			return d
		
		for eintrag in baum.firstChild.childNodes:
			if eintrag.nodeName == "eintrag":
				schluessel = wert = None
			
				for knoten in eintrag.childNodes:
					if knoten.nodeName == "schluessel":
						schluessel = knoten_auslesen(knoten)
					elif knoten.nodeName == "wert":
						wert = knoten_auslesen(knoten)

				d[schluessel] = wert
	
	return d


def erstelle_eintrag(doc, schluessel, wert):
	tag_eintrag = doc.createElement("eintrag")
	tag_schluessel = doc.createElement("schluessel")
	tag_wert = doc.createElement("wert")
	
	tag_schluessel.setAttribute("typ", type(schluessel).__name__)
	tag_wert.setAttribute("typ", type(wert).__name__)
	
	text = doc.createTextNode(str(schluessel))
	tag_schluessel.appendChild(text)
	
	text = doc.createTextNode(str(wert))
	tag_wert.appendChild(text)
	
	tag_eintrag.appendChild(tag_schluessel)
	tag_eintrag.appendChild(tag_wert)
	
	return tag_eintrag


def schreibe_dict(d, dateiname):
	doc = dom.Document()
	#impl = dom.getDOMImplementation()
	#newdoc = impl.createDocument(None, "dictionary", None)
	#tag_dict = dom.Element("dictionary")
	tag_dict = doc.createElement("dictionary")
	#tag_dict = newdoc.documentElement
	#doc.appendChild(tag_dict)
	
	for schluessel, wert in d.items():
		tag_eintrag = erstelle_eintrag(doc, schluessel, wert)
		tag_dict.appendChild(tag_eintrag)
	
	doc.appendChild(tag_dict)
	
	with open(dateiname, "w") as f:
		doc.writexml(f, "", "\t", "\n")


#print(lade_dict("testxml.xml"))
d = lade_dict("testxml.xml")
schreibe_dict(d, "testxml_copy.xml")









