import random

#board = [None, "X", "O", "O", "X", "X", "O", "X", "X", "O"] #for testing purpouses

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
	board[move] = letter[currentMove]

def askMovement(board):
	print('What is your movement?')
	move = input('> ')[0]
	if move.isdigit():
		if move != 0 and posibleMoves(int(move)) == True:
			return move

if True: #use the one below, this is temporaly
#while True:
	board = [" "] * 10
	player, ia = chooseLetter()
	turn = whoGoesFirst()
	ingame = True
	if ingame is True: #same as below, use while when fully developed
		if turn is 0:
			print('Your turn!')
			move = askMovement(board)
			print(move)
			exit(0)
		if turn is 1:
			print('IA turn')
			exit(0)
