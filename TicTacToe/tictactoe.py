#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tictactoe.py
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

# Code stammt von folgender Seite
# http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python

import sys
print sys.version


choices = []
playerOneTurn = True
winner = False
count = 0

for x in range(0, 9):
	choices.append(str(x + 1))

def printBoard():
	print '\n -----'
	print '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|'
	print ' -----'
	print '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|'
	print ' -----'
	print '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|'
	print ' -----\n'


while not winner:
	printBoard()
	
	if playerOneTurn:
		print 'Player 1: '
	else:
		print 'Player 2: '

	choice = int(input(">> "))
	
	if playerOneTurn:
		choices[choice - 1] = 'X'
	else:
		choices[choice - 1] = 'O'

	playerOneTurn = not playerOneTurn
	
	for x in range(0, 3):
		y = x * 3
		if (choices[y] == choices[y + 1] and choices[y] == choices[y + 2]):
			winner = True
		
		if (choices[x] == choices[x + 3] and choices[x] == choices[x + 6]):
			winner = True
	
	if ((choices[0] == choices[4] and choices[0] == choices[8]) or
	(choices[2] == choices[4] and choices[0] == choices[6])):
		winner = True
	
	count += 1
	if (count == 9):
		break

	printBoard()

printBoard()

if (winner):
	print "Player " + str(int(playerOneTurn) + 1) + " wins!\n"
else:
	print "No Winner!"


















