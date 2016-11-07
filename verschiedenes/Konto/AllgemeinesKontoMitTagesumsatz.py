#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AllgemeinesKontoMitTagesumsatz.py
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

import AllgemeinesKonto

class AllgemeinesKontoMitTagesumsatz(AllgemeinesKonto.AllgemeinesKonto):
	def __init__(self, kundendaten, kontostand, max_tagesumsatz = 1500):
		AllgemeinesKonto.AllgemeinesKonto.__init__(self, kundendaten, kontostand)
		self.MaxTagesumsatz = max_tagesumsatz
		self.UmsatzHeute = 0.0
	
	def transferMoeglich(self, betrag):
		return (self.UmsatzHeute + betrag <= self.MaxTagesumsatz)
	
	def auszahlenMoeglich(self, betrag):
		return self.transferMoeglich(betrag)
	
	def einzahlenMoeglich(self, betrag):
		return self.transferMoeglich(betrag)
	
	def einzahlen(self, betrag):
		if AllgemeinesKonto.AllgemeinesKonto.einzahlen(self, betrag):
			self.UmsatzHeute += betrag
			return True
		else:
			return False
	
	def auszahlen(self, betrag):
		if AllgemeinesKonto.AllgemeinesKonto.auszahlen(self, betrag):
			self.UmsatzHeute += betrag
			return True
		else:
			return False
	
	def zeige(self):
		AllgemeinesKonto.AllgemeinesKonto.zeige(self)
		print("Heute schon {:.2f} von {:.2f} Euro umgesetzt".format(self.UmsatzHeute, self.MaxTagesumsatz))
	
