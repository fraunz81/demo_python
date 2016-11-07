#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kontoMain.py
#  
#  Copyright 2014 Franz Habison <habison.franz@gmx.at>
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

import konto
import ckonto


k1 = konto.neuesKonto("Heinz Meier", 567123, 12350.0)
k2 = konto.neuesKonto("Erwin Schmidt", 396754, 15000.0)
print(konto.transferGeld(k1, k2, 160))
print(konto.transferGeld(k2, k1, 1000))
print(konto.transferGeld(k2, k1, 500))
print(konto.einzahlen(k2, 500))
konto.zeigeKonto(k1)
konto.zeigeKonto(k2)
print (50 * "*")

k1 = ckonto.CKonto("Heinz Meier", 567123, 12350.0)
k2 = ckonto.CKonto("Erwin Schmidt", 396754, 15000.0)
print(k1.transferGeld(k2, 160))
print(k2.transferGeld(k1, 1000))
print(k2.transferGeld(k1, 500))
print(k2.einzahlen(500))
k1.zeige()
k2.zeige()


k1 = ckonto.CKonto("Dagobert Duck", 1337, 99999999999999999999)
k2 = ckonto.CKonto("Donald Duck", 1337, 1.5)
k3 = ckonto.CKonto("Gustav Gans", 2674, 50000)

print(k1 == k2)
print(k1 == k3)
