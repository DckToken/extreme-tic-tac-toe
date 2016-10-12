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

printBoard()
