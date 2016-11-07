#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

import GirokontoMitTagesumsatz
import Nummernkonto
import NummernkontoMitTagesumsatz

k1 = GirokontoMitTagesumsatz.GirokontoMitTagesumsatz("Heinz Meier", 567123, 12350.0)
k2 = GirokontoMitTagesumsatz.GirokontoMitTagesumsatz("Erwin Schmidt", 396754, 15000.0)

k1.geldtransfer(k2, 160)
k2.geldtransfer(k1, 1000)
k2.geldtransfer(k1, 500)
k2.einzahlen(500)

k1.zeige()
k2.zeige()


nk1 = Nummernkonto.Nummernkonto(1122334455, 5000)
nk2 = NummernkontoMitTagesumsatz.NummernkontoMitTagesumsatz(9988776655, 12000, 3000)

nk1.auszahlen(1000)
nk2.einzahlen(1500)

nk1.geldtransfer(nk2, 2000)

nk1.zeige()
nk2.zeige()
