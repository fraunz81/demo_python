#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  recipeFrame.py
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
import recipeList


class RecipeFrame(tkinter.Frame):
	def __init__(self, master = None):
		tkinter.Frame.__init__(self, master)
		#self.pack()
		self.createWidgets()
	
	
	def createWidgets(self):
		#Titel
		self.lbTitle, self.txtTitle = self.createLabelEntry(self, "Titel: ", 0, 0)
		#Portionen
		self.lbPortion, self.txtPortion = self.createLabelEntry(self, "Portionen: ", 1, 0)
		#Zubereitungszeit
		self.lbPreparationTime, self.txtPreparationTime = self.createLabelEntry(self, "Zubereitungszeit: ", 2, 0)
		#Backzeit
		self.lbBackTime, self.txtBackTime = self.createLabelEntry(self, "Backzeit: ", 3, 0)
		#Kühlzeit
		self.lbCoolingTime, self.txtCoolingTime = self.createLabelEntry(self, "Kühlzeit: ", 4, 0)
		#Kochzeit
		self.lbCookingTime, self.txtCookingTime = self.createLabelEntry(self, "Kochzeit: ", 5, 0)
		#Schwierigkeit
		self.lbDifficulty, self.txtDificulty = self.createLabelEntry(self, "Schwierigkeit: ", 6, 0)
		#Zutaten:
		self.sectionIngredients(7, 0)
		
	def sectionIngredients(self, row, col):
		self.lbfIngredients = tkinter.LabelFrame(self, text="Zutaten erfassen", padx=5, pady=5)
		self.lbfIngredients.grid(row = row, column = col, columnspan=2, rowspan=2, sticky = tkinter.W)
		#Buttons Ändern und Hinzufügen
		bChange = tkinter.Button(self.lbfIngredients, text="Ändern", command=self.changeIngredients)
		bChange.grid(row = 0, column = 0)
		bAdd = tkinter.Button(self.lbfIngredients, text="Hinzufügen", command=self.changeIngredients)
		bAdd.grid(row = 0, column = 1)
		#Radiobutton - Überschrift, Zutat
		choices = ("Überschrift", "Zutat")
		choicesVar = tkinter.StringVar()
		choicesVar.set("Zutat")
		i = 1
		for text in choices:
			b = tkinter.Radiobutton(self.lbfIngredients, text=text, variable=choicesVar, value=text, command = self.changeIngredients)
			b.grid(row = i, column = 0, sticky = tkinter.W)
			i += 1
		#Zutat
		varTxt = tkinter.StringVar()
		varTxt.set("Zutat")
		txtIngredient = tkinter.Entry(self.lbfIngredients, textvariable=varTxt)
		#i += 1
		txtIngredient.grid(row = 1, column = 1, rowspan = 2)
		#Zusammenfassung der Zutaten
		row += 1
		self.sumIngredients = recipeList.RecipeList(self.lbfIngredients)
		self.sumIngredients.grid(row = row, column = 1, rowspan = 2)
		
		
		
	def createLabelEntry(self, parent, lbtxt, row, col):
		lb = tkinter.Label(parent, text = lbtxt)
		lb.grid(row = row, column = col, sticky = tkinter.W)
		txt = tkinter.Entry(parent)
		txt.grid(row = row, column = col + 1)
		return lb, txt


	def changeIngredients(self, *event):
		print("Zutat ändern")



















