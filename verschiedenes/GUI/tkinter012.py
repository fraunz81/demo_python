#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkinter012.py
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

def textChanged(event):
	print("Text: {0}".format(txt.get("1.0", "end")))


master = tkinter.Tk()
#Listbox
lb = tkinter.Listbox(master)
lb.pack(side = "left")
#Scrollbar in Listbox
sb = tkinter.Scrollbar(master)
sb.pack(fill = "y", side = "left")
lb.insert("end", *[i * i for i in range(50)])
lb["yscrollcommand"] = sb.set
sb["command"] = lb.yview

#Spinbox
spin = tkinter.Spinbox(master)
spin["from"] = 0
spin["to"] = 100
spin.pack()

#Spinbox mit vorgegebenen Werten
spin2 = tkinter.Spinbox(master)
#spin2["values"] = (2, 3, 5, 7, 11, 13)
spin2["values"] = ("A", "B", "C")
spin2.pack()

#Text-Widget
txt = tkinter.Text(master)
txt.pack()
txt.tag_config("o", foreground="orange")
txt.tag_config("u", underline=True)

txt.insert("end", "Hallo Welt\n")
txt.insert("end", "Dies ist ein langer, oranger Text\n", "o")
txt.insert("end", "Und unterstrichen ebenfalls", "u")

txt.bind("<KeyRelease>", textChanged)



master.mainloop()






















