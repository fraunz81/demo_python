#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ckonto.py
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


class CKonto:
	def __init__(self, inhaber, kontonummer, kontostand, maxTagesumsatz = 1500):
		self.Inhaber = inhaber
		self.Kontonummer = kontonummer
		self.Kontostand = kontostand
		self.MaxTagesumsatz = maxTagesumsatz
		self.UmsatzHeute = 0

	def transferGeld(self, ziel, betrag):
		# Hier erfolgt der Test, ob der Tansfer möglich ist
		if (betrag < 0 or 
			self.UmsatzHeute + betrag > self.MaxTagesumsatz or
			ziel.UmsatzHeute + betrag > ziel.MaxTagesumsatz):
			# Transfer unmöglich
			return False
		else:
			# Alles OK - Auf geht's
			self.Kontostand -= betrag
			self.UmsatzHeute += betrag
			ziel.Kontostand += betrag
			ziel.UmsatzHeute += betrag
			return True
	
	def einzahlen(self, betrag):
		if (betrag < 0 or self.UmsatzHeute + betrag > self.MaxTagesumsatz):
			# Tageslimit überschritten oder ungültiger Betrag
			return False
		else:
			self.Kontostand += betrag
			self.UmsatzHeute += betrag
			return True
	
	def auszahlen(self, betrag):
		if (betrag < 0 or self.UmsatzHeute + betrag > self.MaxTagesumsatz):
			# Tageslimit überschritten oder ungültiger Betrag
			return False
		else:
			self.Kontostand -= betrag
			self.UmsatzHeute += betrag
			return True
	
	def zeige(self):
		print("Konto von {0}".format(self.Inhaber))
		print("Aktueller Kontostand: {0:.2f} Euro".format(self.Kontostand))
		print("Heute schon {0:.2f} von {1} Euro umgesetzt".format(self.UmsatzHeute, self.MaxTagesumsatz))
	
	def __eq__(self, k2):
		return self.Kontonummer == k2.Kontonummer






