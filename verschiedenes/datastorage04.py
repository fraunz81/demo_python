#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  datastorage04.py
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


from xml.dom.minidom import Document

#create minidom-document
doc = Document()

# create base element
base = doc.createElement('Dictionary')
doc.appendChild(base)

# create an entry element
entry = doc.createElement('Entry')

# ... and append it to the base element
base.appendChild(entry)

# create another element 
german = doc.createElement('German')

# create content
german_content = doc.createTextNode('Hund')

# append content to element
german.appendChild(german_content)

# append the german entry to our entry element
entry.appendChild(german)

# now the same with an english entry
english = doc.createElement('English')
english_content = doc.createTextNode('dog')
english.appendChild(english_content)
entry.appendChild(english)

#print(doc.toxml(encoding='utf-8'))
print(doc.toprettyxml())
