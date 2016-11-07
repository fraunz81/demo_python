#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  konto.py
#  
#  Copyright 2014 Franz Habison <habison.franz@gmx.at>
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


# ein Beispiel
#konto = {
#	"Inhaber" : "Hans Meier",
#	"Kontonummer" : 567123,
#	"Kontostand" : 12350.0,
#	"MaxTagesumsatz" : 1500,
#	"UmsatzHeute" : 10.0
#}

def neuesKonto(inhaber, kontonummer, kontostand, maxTagesumsatz = 1500):
	return {
		"Inhaber" : inhaber,
		"Kontonummer" : kontonummer,
		"Kontostand" : kontostand,
		"MaxTagesumsatz" : maxTagesumsatz,
		"UmsatzHeute" : 0
		}

def transferGeld(quelle, ziel, betrag):
	# Hier erfolgt der Test, ob der Tansfer möglich ist
	if (betrag < 0 or 
		quelle["UmsatzHeute"] + betrag > quelle["MaxTagesumsatz"] or
		ziel["UmsatzHeute"] + betrag > ziel["MaxTagesumsatz"]):
		# Transfer unmöglich
		return False
	else:
		# Alles OK - Auf geht's
		quelle["Kontostand"] -= betrag
		quelle["UmsatzHeute"] += betrag
		ziel["Kontostand"] += betrag
		ziel["UmsatzHeute"] += betrag
		return True

def einzahlen(konto, betrag):
	if (betrag < 0 or konto["UmsatzHeute"] + betrag > konto["MaxTagesumsatz"]):
		# Tageslimit überschritten oder ungültiger Betrag
		return False
	else:
		konto["Kontostand"] += betrag
		konto["UmsatzHeute"] += betrag
		return True

def auszahlen(konto, betrag):
	if (betrag < 0 or konto["UmsatzHeute"] + betrag > konto["MaxTagesumsatz"]):
		# Tageslimit überschritten oder ungültiger Betrag
		return False
	else:
		konto["Kontostand"] -= betrag
		konto["UmsatzHeute"] += betrag
		return True

def zeigeKonto(konto):
	print("Konto von {0}".format(konto["Inhaber"]))
	print("Aktueller Kontostand: {0:.2f} Euro".format(konto["Kontostand"]))
	print("Heute schon {0:.2f} von {1} Euro umgesetzt".format(konto["UmsatzHeute"], konto["MaxTagesumsatz"]) )



