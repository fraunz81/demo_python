#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  database01.py
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


import sqlite3 as sql3

#Wenn man eine SQL-Db nur im Speicher benötigt
#connection = sql3.connect(":memory:")

def create_tables(cursor):
	create_table_lager = """CREATE TABLE lager (
		fachnummer INTEGER, 
		seriennummer INTEGER, 
		komponente TEXT,
		lieferant TEXT, 
		reserviert INTEGER)"""

	create_table_lieferant = """CREATE TABLE lieferanten (
		kurzname TEXT,
		name TEXT,
		telefonnummer TEXT)"""

	create_table_kunden = """CREATE TABLE kunden (
		kundennummer INTEGER,
		name TEXT,
		anschrift TEXT)"""

	cursor.execute(create_table_lager)
	cursor.execute(create_table_lieferant)
	cursor.execute(create_table_kunden)
	

def fill_tables(cursor):
	werte = ("DR", "Danger Electronics", "123456")
	sql = "INSERT INTO lieferanten VALUES (?, ?, ?)"
	cursor.execute(sql, werte)

	for row in (	(1, "2607871987", "Grafikkarte Typ 1", "FC", 0),
						(2, "19870109", "Prozessor Typ 13", "LPE", 57),
						(10, "06198823", "Netzteil Typ 3", "FC", 0),
						(25, "11198703", "LED-Lüfter", "FC", 57),
						(26, "19880105", "Festplatte 128 GB", "LPE", 12)
					):
		cursor.execute("INSERT INTO lager VALUES(?, ?, ?, ?, ?)", row)
	
	lieferanten = (("FC", "FiboComputing Inc.", "011235813"),
						("LPE", "LettgenPetersErnesti", "026741337"),
						("GC", "Golden Computers", "016180339"))
	cursor.executemany("INSERT INTO lieferanten VALUES (?, ?, ?)", lieferanten)
	
	kunden = ((12, "Heinz Elhurg", "Turnhallenstr. 1, 3763 Sporthausen"),
				(57, "Markus Altbert", "Kämperwerg 24, 2463 Duisschloss"),
				(64, "Steve Apple", "Podmacstr 2, 7467 Iwarhausen"))
	cursor.executemany("INSERT INTO kunden VALUES (?, ?, ?)", kunden)





connection = sql3.connect("lagerverwaltung.db")
cursor = connection.cursor()
#create_tables(cursor)
#fill_tables(cursor)
#connection.commit()

#cursor.execute("SELECT fachnummer, komponente FROM lager")
#cursor.execute("SELECT fachnummer, komponente FROM lager WHERE reserviert = 0")
#cursor.execute("SELECT fachnummer, komponente FROM lager WHERE reserviert = 0 AND lieferant = 'FC'")
#print(cursor.fetchall())

#cursor.execute("SELECT * FROM kunden")
#print(cursor.fetchall())

#sql = """SELECT lager.fachnummer, lager.komponente, lieferanten.name
#			FROM lager, lieferanten
#			WHERE lieferanten.telefonnummer = '011235813'"""
#cursor.execute(sql)
#print(cursor.fetchall())

# Die eher unübliche Variante des zeilenweisen einlesens
#cursor.execute("SELECT * FROM kunden")
#row = cursor.fetchone()
#while row:
#	print(row)
#	row = cursor.fetchone()

# Die "elegantere" Art zeilenweise das Ergebnis einzulesen
#for row in cursor:
#	print(row)

'''
# Eigene Funktion definieren für Textdaten aus der Db zu verändern
def my_text_factory(value):
	return str(value, "utf-8", "ignore").upper()


connection.text_factory = my_text_factory
cursor = connection.cursor()
cursor.execute("SELECT * FROM kunden")
print(cursor.fetchall())
'''

# Eigene Funktion für row_factory
#cursor.execute("SELECT * FROM kunden")
# So sieht die description für die Tabelle Kunden aus.
#cursor.description(	('kundennummer', None, None, None, None, None, None),
#							('name', None, None, None, None, None, None),
#							('anschrift', None, None, None, None, None, None))

def zeilen_dict(cursor, zeile):
	ergebnis = {}
	for spaltennr, spalte in enumerate(cursor.description):
		ergebnis[spalte[0]] = zeile[spaltennr]
	
	return ergebnis


connection.row_factory = zeilen_dict
cursor = connection.cursor()
cursor.execute("SELECT * FROM kunden")
print(cursor.fetchall())












