import random

#board = [None, "X", "O", "O", "X", "X", "O", "X", "X", "O"] #for testing purpouses

def printBoard(board):
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

def checkWinner(bo, le):
    return ((board[7] == letter and board[8] == letter and board[9] == le) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == le) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == le) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == le) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == le) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == le) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == le) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == le)) # diagonal

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
	#randomly chooses who goes first
	firstMove = random.randint(0, 1)
	if firstMove is 0:
		return "player"
	else:
		return "ia"
	return firstMove

def placeMove(move, letter, board):
	board[int(move)] = letter

def askMovement(board):
	print('What is your movement?')
	move = input('> ')[0]
	if move.isdigit():
		if move != 0 and posibleMoves(int(move)) == True:
			return move

if True: #use the one below, this is temporaly
#while True:
	board = [" "] * 10
	player_letter, ia_letter = chooseLetter()
	turn = whoGoesFirst()
	ingame = True
	if ingame is True: #same as below, use while when fully developed
		if turn is "player":
			print('Your turn!')
			printBoard(board)
			move = askMovement(board)
			print(move)
			placeMove(move, player_letter, board)
			printBoard(board)
			exit(0)
		if turn is "ia":
			print('IA turn')
			exit(0)
