#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  threading05.py
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



import threading

class PrimzahlThread(threading.Thread):
	Ergebnis = {}
	ErgebnisLock = threading.Lock()

	def __init__(self, zahl):
		threading.Thread.__init__(self)
		self.zahl = zahl
		
		PrimzahlThread.ErgebnisLock.acquire()
		PrimzahlThread.Ergebnis[zahl] = "in Arbeit"
		PrimzahlThread.ErgebnisLock.release()
	
	
	def run(self):
		i = 2
		while i * i <= self.zahl + 1:
			if self.zahl % i == 0:
				ergebnis = "{0} * {1}".format(i, self.zahl / i)

				PrimzahlThread.ErgebnisLock.acquire()
				PrimzahlThread.Ergebnis[self.zahl] = ergebnis
				PrimzahlThread.ErgebnisLock.release()

				return
			
			i += 1

		PrimzahlThread.ErgebnisLock.acquire()
		PrimzahlThread.Ergebnis[self.zahl] = "prim"
		PrimzahlThread.ErgebnisLock.release()


meine_threads = []

eingabe = input("> ")
while eingabe != "ende":
	if eingabe == "status":
		print("-" * 10 + " Aktueller Status " + "-" * 10)
		PrimzahlThread.ErgebnisLock.acquire()
		for z, e in PrimzahlThread.Ergebnis.items():
			print("{0} = {1}".format(z, e))
		
		PrimzahlThread.ErgebnisLock.release()
		print("-" * 38)
	elif int(eingabe) not in PrimzahlThread.Ergebnis:
		thread = PrimzahlThread(int(eingabe))
		meine_threads.append(thread)
		thread.start()
	
	eingabe = input("> ")

for t in meine_threads:
	t.join()


