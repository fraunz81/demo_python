#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  App.py
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
import appmenu
import recipeList
import statusBar
import toolbar


class App(tkinter.Frame):
	def __init__(self, master = None):
		tkinter.Frame.__init__(self, master)
		master.title("Rezepthek")
		
		#self.parent = master
		self.pack()
		
		#Menü
		self.appm = appmenu.AppMenu(self)
		master.config(menu = self.appm)
		#Widgets
		self.createWidgets()

	def createWidgets(self):
		#Toolbar
		self.toolbar = toolbar.Toolbar(self)
		self.toolbar.pack(side = tkinter.TOP, fill = tkinter.X)
		#Listbox mit Scrollbar für die Anzeige der Rezepte
		self.sb = recipeList.RecipeList(self)
		self.sb.pack()
		#Statusbar
		self.status = statusBar.StatusBar(self)
		self.status.pack(side = tkinter.BOTTOM, fill = tkinter.X)
		
		

if __name__ == "__main__":
	master = tkinter.Tk()
	#myApp = App(master)
	myApp = App(master)
	myApp.mainloop()
