#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ExceptionHandling.py
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

def get(name):
	return open(name)


def get1(name):
	try:
		return open(name)
	except IOError:
		return None


def get2(name):
	try:
		return open(name)
	except (IOError, TypeError):
		return None


def get3(name):
	try:
		return open(name)
	except IOError:
		return None
	except TypeError:
		return None


def get4(name):
	try:
		return open(name)
	except:
		return None


def get5(name):
	try:
		return open(name)
	except (IOError, TypeError) as e:
		print("Fehlermeldung: ", e.args[0])









