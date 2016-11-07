#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DemoApp002.py
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


import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        #self.newWindow = tk.Toplevel(self.master)
        #self.app = Demo2(self.newWindow)
        self.app = Demo2(self.master)

class Demo2(tk.Toplevel):     
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.title("Demo 2")
        self.button = tk.Button(self, text="Button 2", # specified self as master
                                width=25, command=self.close_window)
        self.button.pack()

    def close_window(self):
        self.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
