#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  threading01.py
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


import _thread

def naehere_pi_an(n):
	pi_halbe = 1
	zaehler, nenner = 2.0, 1.0
	
	for i in range(n):
		pi_halbe *= zaehler / nenner
		if i % 2:
			zaehler += 2
		else:
			nenner += 2
	
	print("Annäherung mit {} Faktoren: {:.16f}".format(n, 2 * pi_halbe))

_thread.start_new_thread(naehere_pi_an, (1111111,))
_thread.start_new_thread(naehere_pi_an, (3111111,))
_thread.start_new_thread(naehere_pi_an, (4111111,))
_thread.start_new_thread(naehere_pi_an, (5111111,))
_thread.start_new_thread(naehere_pi_an, (3211111,))
_thread.start_new_thread(naehere_pi_an, (4111111,))
_thread.start_new_thread(naehere_pi_an, (11111111,))

while True:
	pass
