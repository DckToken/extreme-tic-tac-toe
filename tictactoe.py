import random

#board = ["X", "O", "O", "X", "X", "O", "X", "X", "O"] #for testing purpouses
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]

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
	print('Do you want to be X or O?')
	userInput = input().upper()
	if userInput == "X":
		letter = ["X", "O"]
		global letter
	if userInput == "O":
		letter = ["O", "X"]
		global letter
	else:
		print('Invalid input')
		chooseLetter()

def whoGoesFirst():
	#randomly chooses who goes first (with a 0 for user and 1 for ia)
	print('Randomly choosing who goes first...')
	firstMove = random.randint(0, 1)
	if firstMove == 0:
		print('You go first!')
	if firstMove == 1:
		print('IA goes first')
	currentMove = firstMove
	global currentMove

def placeMove(move):
	board[move] = letter[currentMove]

def movement():
	print('What is your movement?')
	move = int(input())
	placeMove(move)

def game():
	printBoard()
	chooseLetter()
	whoGoesFirst()
	if currentMove == 0:
		movement()
		printBoard()
	else:
		print('WIP')

game()
