#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  database02.py
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



import sqlite3

class Kreis:
	def __init__(self, mx, my, r):
		self.mx = mx
		self.my = my
		self.r = r

#Daten (Objekt) in String konvertieren = Adaption
def kreisadapter(k):
	return "{0};{1};{2}".format(k.mx, k.my, k.r)


#String zu Daten (Objekt) konvertieren = Konvertierung
def kreiskonverter(bytestring):
	mx, my, r = bytestring.split(b";")
	return Kreis(float(mx), float(my), float(r))

#Adapter und Konverter registrieren
sqlite3.register_adapter(Kreis, kreisadapter)
sqlite3.register_converter("KREIS", kreiskonverter)

# Hier wird eine Beispieldatenbank im Arbeitsspeicher mit
# einer einspaltigen Tabelle für Kreise definiert
connection = sqlite3.connect(":memory:", detect_types = sqlite3.PARSE_DECLTYPES)
cursor = connection.cursor()
cursor.execute("CREATE TABLE kreis_tabelle(k KREIS)")

# Kreis in die Datenbank schreiben
kreis = Kreis(1, 2.5, 3)
cursor.execute("INSERT INTO kreis_tabelle VALUES(?)", (kreis,))

# Kreis wider auslesen
cursor.execute("SELECT * FROM kreis_tabelle")

gelesener_kreis = cursor.fetchall()[0][0]
print(type(gelesener_kreis))
print(gelesener_kreis.mx, gelesener_kreis.my, gelesener_kreis.r)























