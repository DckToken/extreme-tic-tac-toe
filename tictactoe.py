import random

board = ["X", "O", "O", "X", "X", "O", "X", "X", "O"]

def printBoard():
	print('   |   |')
	print(' ' + board[8] + ' | ' + board[7] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
	print('   |   |')

def chooseLetter():
	print('Do you want to be X or Y?')
	letter = str(input().upper())
	if letter == "X" or letter == "Y":
		print('[DEBUG] You did good')
		return
	else:
		print('Invalid input')
		chooseLetter()

printBoard()
chooseLetter()
