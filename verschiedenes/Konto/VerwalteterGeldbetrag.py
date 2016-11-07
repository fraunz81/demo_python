#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  VerwalteterGeldbetrag.py
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


class VerwalteterGeldbetrag:
	def __init__(self, anfangsbetrag):
		self.Betrag = anfangsbetrag
	
	def einzahlenMoeglich(self, betrag):
		return True
	
	def auszahlenMoeglich(self, betrag):
		return True
	
	def einzahlen(self, betrag):
		if betrag < 0 or not self.einzahlenMoeglich(betrag):
			return False
		else:
			self.Betrag += betrag
			return True
	
	def auszahlen(self, betrag):
		if betrag < 0 or not self.auszahlenMoeglich(betrag):
			return False
		else:
			self.Betrag += betrag
			return True
	
	def zeige(self):
		print("Betrag: {:.2f}".format(self.Betrag))

