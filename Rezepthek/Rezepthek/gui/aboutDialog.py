#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  aboutDialog.py
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


class AboutDialog(tkinter.Toplevel):
	def __init__(self, master = None):
		tkinter.Toplevel.__init__(self, master)
		self.title("Über die Rezethek")
		#self.pack()
		self.createWidgets()

	def createWidgets(self):
		about_message = "Hier wird Ihnen geholfen."
		msg = tkinter.Message(self, text=about_message)
		msg.pack()

		button = tkinter.Button(self, text="Schließen", command=self.destroy)
		button.pack()






















