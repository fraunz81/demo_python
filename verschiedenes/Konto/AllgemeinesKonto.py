#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AllgemeinesKonto.py
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

import VerwalteterGeldbetrag

class AllgemeinesKonto(VerwalteterGeldbetrag.VerwalteterGeldbetrag):
	def __init__(self, kundendaten, kontostand):
		VerwalteterGeldbetrag.VerwalteterGeldbetrag.__init__(self, kontostand)
		self.Kundendaten = kundendaten
	
	def geldtransfer(self, ziel, betrag):
		if (self.auszahlenMoeglich(betrag) and ziel.einzahlenMoeglich(betrag)):
			self.auszahlen(betrag)
			ziel.einzahlen(betrag)
			return True
		else:
			return False
	
	def zeige(self):
		self.Kundendaten.zeige()
		VerwalteterGeldbetrag.VerwalteterGeldbetrag.zeige(self)

