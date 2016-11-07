#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hello.py
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

#Beispiel stammt von dieser Seite
# http://bottlepy.org/docs/stable/tutorial.html

from bottle import route, run

@route('/hello')
def hello():
	return "Hello World!"

def main():
	run(host='localhost', port=8000, debug=True)
	return 0

if __name__ == '__main__':
	main()

