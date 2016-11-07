#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Rezepthek.py
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

import os, sys

def loadPackage(folder):
	abspath = lambda *p : os.path.abspath(os.path.join(*p))
	#print(abspath)
	PROJECT_ROOT = abspath(os.path.dirname(__file__) + folder)
	#print(PROJECT_ROOT)
	sys.path.insert(0, PROJECT_ROOT)

import tkinter

loadPackage("gui")
import gui.app



master = tkinter.Tk()
myApp = gui.app.App(master)
myApp.mainloop()
