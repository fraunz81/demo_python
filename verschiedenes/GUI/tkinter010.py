#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkinter010.py
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
		self.pack()
		
		self.eintraege = ["Berlin", "London", "Moskau", "Ottawa", "Paris", "Rom", "Tokio", "Washington DC"]
		
		self.lb = tkinter.Listbox(self)
		self.lb.pack(fill="both", expand = "true")
		self.lb["selectmode"] = "extended"
		self.lb.insert("end", *self.eintraege)
		self.lb.bind("<<ListboxSelect>>", self.selectionChanged)
		self.lb.selection_set(0)
		
		self.label = tkinter.Label(self)
		self.label.pack()
		self.selectionChanged(None)

	def selectionChanged(self, event):
		self.label["text"] = "Wir fahren nach: " + ", ".join((self.lb.get(i) for i in self.lb.curselection()))



master = tkinter.Tk()
myapp = MyApp(master)
myapp.mainloop()


























