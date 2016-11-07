#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  visitenkarte.py
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

def leseDatei(datei):
	d = {}
	f = open(datei)
	for zeile in f:
		if ":" in zeile:
			key, d[key] = (s.strip() for s in zeile.split(":", 1))
		elif "key" in locals():
			d[key] += "\n{0}".format(zeile.strip())
	
	f.close()
	return d

regexp = {
	"Name" : r"([A-Za-z]+)\s([A-Za-z]+)",
	"Addr" : r"([A-Za-zß]+)\s(\d+)\s*(\d{4,})\s([A-Za-zß]+)",
	"Tel"  : r"(\+\d{2})\s(\d{3,4})\s(\d{3,})"
}

def analysiereDaten(daten, regexp):
	for key in daten:
		#print("Key: {0}\tDaten: {1}".format(key, daten[key]))
		if key not in regexp:
			return False
		
		m = re.match(regexp[key], daten[key])
		if not m:
			return False
		
		daten[key] = m.groups()
	
	return True


daten = leseDatei("visit01.txt")
#print(daten)
if analysiereDaten(daten, regexp):
	print(daten)
else:
	print("Die Angaben sind fehlerhaft")
