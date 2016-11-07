#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkinter001.py
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
		self.pack();
		self.createWidgets()
	
	
	def createWidgets(self):
		self.nameEntry = tkinter.Entry(self)
		self.nameEntry.pack()
		
		self.name = tkinter.StringVar()
		self.name.set("Ihr Name ...")
		self.nameEntry["textvariable"] = self.name
		
		self.ok = tkinter.Button(self)
		self.ok["text"] = "Ok"
		self.ok["command"] = self.quit
		self.ok.pack(side = "right")
		
		self.rev = tkinter.Button(self)
		self.rev["text"] = "Umdrehen"
		self.rev["command"] = self.onReverse
		self.rev.pack(side = "right")
	
	
	def onReverse(self):
		self.name.set(self.name.get()[::-1])



root = tkinter.Tk()
app = MyApp(root)
app.mainloop()





