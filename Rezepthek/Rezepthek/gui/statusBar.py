#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  statusBar.py
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

class StatusBar(tkinter.Frame):

	def __init__(self, master):
		tkinter.Frame.__init__(self, master)
		self.label = tkinter.Label(self, bd = 1, relief = tkinter.SUNKEN, anchor = tkinter.W)
		self.label.pack(fill = tkinter.X)

	def set(self, format, *args):
		self.label.config(text = format % args)
		self.label.update_idletasks()

	def clear(self):
		self.label.config(text = "")
		self.label.update_idletasks()





