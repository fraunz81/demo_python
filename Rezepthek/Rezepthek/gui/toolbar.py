#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  toolbar.py
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


class Toolbar(tkinter.Frame):
	def __init__(self, master = None):
		tkinter.Frame.__init__(self, master, borderwidth = 0)
		#self.borderwidth = 20
		self.pack()
		self.createWidgets()
	
	def createWidgets(self):
		#To display an icon, you can use the PhotoImage constructor to load a small image from disk, and use the image option to display it.
		b = tkinter.Button(self, text = "new", width = 6, command = self.callback)
		b.pack(side = tkinter.LEFT, padx = 2, pady = 2)

		b = tkinter.Button(self, text = "open", width = 6, command = self.callback)
		b.pack(side = tkinter.LEFT, padx = 2, pady = 2)

	def callback(self, *event):
		print("call the callback")








