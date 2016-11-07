#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkinter011.py
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


import tkinter

class MyApp(tkinter.Frame):
	def __init__(self, master = None):
		tkinter.Frame.__init__(self, master)
		#Menü init
		self.menuBar = tkinter.Menu(master)
		master.config(menu = self.menuBar)
		self.createMenuBar()
		
		#Menübutton
		#self.mb = tkinter.Menubutton(master, text = "Hallo Welt")
		#self.menuButton = tkinter.Menu(self.mb, tearoff = False)
		#self.menuButton.add_checkbutton(label = "Donald Duck")
		#self.menuButton.add_checkbutton(label = "Dagobert Duck")
		#self.menuButton.add_checkbutton(label = "Tick, Trick und Track")
		#self.mb["menu"] = self.menuButton
		#self.mb.pack()
		
		#OptionMenu
		#lst = ["Linux", "MacOS X", "Windows"]
		#var = tkinter.StringVar()
		#self.op = tkinter.OptionMenu(master, var, *lst)
		#var.set("Linux")
		#self.op.pack()

	def createMenuBar(self):
		self.menuFile = tkinter.Menu(self.menuBar, tearoff = False)
		self.menuFile.add_command(label = "Öffnen", command = self.handler)
		self.menuFile.add_command(label = "Speichern", command = self.handler)
		self.menuFile.add_command(label = "Speichern unter", command = self.handler)
		self.menuFile.add_separator()
		self.menuFile.add_command(label = "Beenden", command = self.quit)
		
		self.menuBar.add_cascade(label = "Datei", menu = self.menuFile)
	
	def handler(self, *event):
		print("Hallo")


master = tkinter.Tk()
app = MyApp(master)
app.mainloop()






























