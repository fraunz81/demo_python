#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  threading06.py
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
import queue

class Mathematiker(threading.Thread):
	Ergebnis = {}
	ErgebnisLock = threading.Lock()
	Briefkasten = queue.Queue()
	
	def run(self):
		while True:
			zahl = Mathematiker.Briefkasten.get()
			ergebnis = self.istPrimzahl(zahl)
			
			Mathematiker.ErgebnisLock.acquire()
			Mathematiker.Ergebnis[zahl] = ergebnis
			Mathematiker.ErgebnisLock.release()
			
			Mathematiker.Briefkasten.task_done()


	def istPrimzahl(self, zahl):
		i = 2
		while i * i < zahl + 1:
			if zahl % i == 0:
				return "{0} * {1}".format(zahl, zahl / i)
			
			i += 1
		
		return "prim"



meine_threads = [Mathematiker() for i in range(5)]
for thread in meine_threads:
	thread.setDaemon(True)
	thread.start()

eingabe = input("> ")
while eingabe != "ende":
	if eingabe == "status":
		print("-" * 10 + " Aktueller Status " + "-" * 10)
		Mathematiker.ErgebnisLock.acquire()
		for z, e in Mathematiker.Ergebnis.items():
			print("{0} = {1}".format(z, e))
		
		Mathematiker.ErgebnisLock.release()
		print("-" * 38)
	elif int(eingabe) not in Mathematiker.Ergebnis:
		Mathematiker.ErgebnisLock.acquire()
		Mathematiker.Ergebnis[int(eingabe)] = "in Arbeit"
		Mathematiker.ErgebnisLock.release()
		
		Mathematiker.Briefkasten.put(int(eingabe))
	
	eingabe = input("> ")


Mathematiker.Briefkasten.join()






