import random

#board = [None, "X", "O", "O", "X", "X", "O", "X", "X", "O"] #for testing purpouses
global board
board = [None, " ", " ", " ", " ", " ", " ", " ", " ", " "]

def printBoard():
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def chooseLetter():
	userInput = ""
	while not (userInput == "X" or userInput == "O"):
		print('Do you want to be X or O?')
		userInput = input('> ').upper()
	global letter
	if userInput == "X":
		return ["X", "O"]
	else:
		return ["O", "X"]

def posibleMoves(move):
	return board[move] == " "

def whoGoesFirst():
	#randomly chooses who goes first (with a 0 for user and 1 for ia)
	firstMove = random.randint(0, 1)
	return firstMove

def placeMove(move):
	global board
	board[move] = letter[currentMove]

def askMovement():
	print('What is your movement?')
	move = input('> ')[:1]
	try:
		move = int(move)
	except Exception:
		print('Try again!')
		askMovement()
	else:
		if move != 0 and not posibleMoves(move):
			placeMove(move)

if True: #use the one below, this is temporaly
#while True:
	player, ia = chooseLetter()
	turn = whoGoesFirst()
	ingame = True
	if ingame is True: #same as below, use while when fully developed
		if turn is 0:
			print('Your turn!')
		if turn is 1:
			print('IA turn')