#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkinter004.py
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
	def __init__(self, master):
		tkinter.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		self.createBindings()

	def createWidgets(self):
		self.label = tkinter.Label(self)
		self.label.pack()
		self.label["text"] = "Bitte sende ein Event"
		
		self.entry = tkinter.Entry(self)
		self.entry.pack()
		
		self.ok = tkinter.Button(self)
		self.ok.pack()
		self.ok["text"] = "Beenden"
		self.ok["command"] = self.quit

	def createBindings(self):
		self.entry.bind("Entenhausen", self.eventEntenhausen)
		self.entry.bind("<ButtonPress-1>", self.eventMouseClick)
		self.entry.bind("<MouseWheel>", self.eventMouseWheel)
		self.entry.bind("<Button-4>", self.eventMouseWheelForward)
		self.entry.bind("<Button-5>", self.eventMouseWheelBackward)
	
	def eventEntenhausen(self, event):
		self.label["text"] = "Sie kennen das geheime Passwort!"

	def eventMouseClick(self, event):
		self.label["text"] = "Mausklick an Position ({}, {})".format(event.x, event.y)
	
	def eventMouseWheel(self, event):
		if event.delta < 0:
			self.label["text"] = "Bitte bewegen Sie das Mausrad in die richtige Richtung."
		else:
			self.label["text"] = "Vielen Dank."
	
	def eventMouseWheelForward(self, event):
		self.label["text"] = "Vor vor vor noch ein Tor."
	
	def eventMouseWheelBackward(self, event):
		self.label["text"] = "Zurück die Russen kommen."

'''
Platform differences:

    On Windows, you bind to <MouseWheel> and you need to divide event.delta by 120 
    (or some other factor depending on how fast you want the scroll)
    
    on OSX, you bind to <MouseWheel> and you need to use event.delta without modification
    
    on X11 systems you need to bind to <Button-4> and <Button-5>, 
    and you need to divide event.delta by 120 (or some other factor depending on how fast you want to scroll)
'''

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()















