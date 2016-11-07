#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DemoApp003.py
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




#!/usr/bin/env python
import tkinter as tk

from tkinter import *

class windowclass():
        def __init__(self,master):
                self.master = master
                self.frame = tk.Frame(master)
                self.lbl = Label(master , text = "Label")
                self.lbl.pack()
                self.btn = Button(master , text = "Button" , command = self.command )
                self.btn.pack()
                self.frame.pack()

        def command(self):
                print( 'Button is pressed!')
                self.newWindow = tk.Toplevel(self.master)
                self.app = windowclass1(self.newWindow)


class windowclass1():
        def __init__(self , master):
                self.master = master
                self.frame = tk.Frame(master)
                master.title("a")
                self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25 , command = self.close_window)
                self.quitButton.pack()
                self.frame.pack()

        def close_window(self):
                self.master.destroy()


root = Tk()
root.title("window")
root.geometry("350x50")
cls = windowclass(root)
root.mainloop()

