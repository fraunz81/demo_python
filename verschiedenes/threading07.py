#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  threading07.py
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



import time, threading

def wecker(gestellt):
	print("RIIIIIIIING!!!")
	print("Der Wecker wurde um {0} Uhr gestellt.".format(gestellt))
	print("Es ist {0} Uhr".format(time.strftime("%H:%M:%S")))

timer = threading.Timer(30, wecker, [time.strftime("%H:%M:%S")])
timer.start()

