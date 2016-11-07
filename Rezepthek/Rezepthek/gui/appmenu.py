#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AppMenu.py
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

#import gui.recipeFrame
import recipeFrame
import aboutDialog



class AppMenu(tkinter.Menu):
	def __init__(self, parent):
		tkinter.Menu.__init__(self, parent)
		self.parent = parent
		# Menü erzeugen
		self.createMenuBar()
		

	def createMenuBar(self):
		# Menü Datei
		self.filemenu = tkinter.Menu(self, tearoff=False)
		self.filemenu.add_command(label = "Platzhalter", command = self.Platzhalter)
		self.filemenu.add_separator()
		self.filemenu.add_command(label = "Beenden", command = self.quit)
		self.add_cascade(label = "Datei", menu = self.filemenu)
		
		# Menü Bearbeiten
		self.editmenu = tkinter.Menu(self, tearoff = False)
		self.editmenu.add_command(label = "Ausschneiden", command = self.Cut)
		self.editmenu.add_command(label = "Kopieren", command = self.Copy)
		self.editmenu.add_command(label = "Einfügen", command = self.Paste)
		self.add_cascade(label = "Bearbeiten", menu = self.editmenu)
		
		# Menü Rezept
		self.recipemenu = tkinter.Menu(self, tearoff = False)
		self.recipemenu.add_command(label = "Neu", command = self.newRecipe)
		self.add_cascade(label = "Rezept", menu = self.recipemenu)
		
		# Menü Hilfe
		self.helpmenu = tkinter.Menu(self, tearoff = False)
		self.helpmenu.add_command(label = "About", command = self.About)
		self.add_cascade(label = "Hilfe", menu = self.helpmenu)

	
	def Platzhalter(self, *event):
		#print("Das ist eine Platzhalterfunktion")
		self.parent.status.set("Platzhalterfunktion")
	
	#Menü Bearbeiten
	def Cut(self, *event):
		#print("Sie haben soeben etwas ausgeschnitten")
		self.parent.status.set("cut")
	
	def Copy(self, *event):
		#print("Sie haben soeben etwas kopiert")
		self.parent.status.set("copied")
	
	def Paste(self, *event):
		#print("Sie haben soeben etwas eingefügt")
		self.parent.status.set("paste")
	
	#Menü Rezept
	def newRecipe(self, *event):
		#print("Neues Rezept erstellen ...")
		self.Recipe = tkinter.Toplevel(self.parent)
		#self.app = gui.recipeFrame.RecipeFrame(self.Recipe)
		self.app = recipeFrame.RecipeFrame(self.Recipe)
		self.app.pack()

	
	#Menü Hilfe
	def About(self, *event):
		#print("Aboutmenu")
		#about = tkinter.Toplevel(self.parent)
		aboutDlg = aboutDialog.AboutDialog(self.parent)
		

		
		
