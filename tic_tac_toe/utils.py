import os
import random

def clearScreen():
	"""
	Clears terminal based on user's OS
	"""
	os.system('cls' if os.name=='nt' else 'clear')

def display_board(board):
	"""
	prints the current board
	"""
	print ("TIC TAC TOE			      Move Index\n")
	print (" " + board[0] + " | " + board[1] + " | " + board[2] + "				 " + "7 8 9")
	print ("---|---|---")
	print (" " + board[3] + " | " + board[4] + " | " + board[5] + "				 " + "4 5 6")
	print ("---|---|---")
	print (" " + board[6] + " | " + board[7] + " | " + board[8] + "				 " + "1 2 3")
	print ("")

def display_tutorial_board(board, tut):
	"""
	prints the current board plus the feasibility of each move
	"""
	prob = board[::]
	i = j = 0
	scoreToResult = {1:'W', 0:'D', -1:'L'}
	while j < len(board) :
		if board[j] == '-':
			prob[j] = scoreToResult[tut[i]]
			i += 1
		else:
			prob[j] = '-'
		j += 1

	print ("TIC TAC TOE    		      Move Index		       Winning chance\n")
	print (" " + board[0] + " | " + board[1] + " | " + board[2] + "			 " + "7 8 9" + "				 " + prob[0] + " " + prob[1] + " " + prob[2])
	print ("---|---|---")
	print (" " + board[3] + " | " + board[4] + " | " + board[5] + "			 " + "4 5 6" + "				 " + prob[3] + " " + prob[4] + " " + prob[5])
	print ("---|---|---")
	print (" " + board[6] + " | " + board[7] + " | " + board[8] + "			 " + "1 2 3" + "				 " + prob[6] + " " + prob[7] + " " + prob[8])
	print ("")

def check_empty(board):
	return board.count('-') == 9
	
def check_win(board, player1, player2):
	"""
	returns status of current board: 1-> won, 2-> draw, 0-> game undecided
	if game won, return value is [1,who_won]
	"""
	returned_val = ['', '']
	if   board[0] == board[1] == board[2] and board[0] in [player1, player2]:	returned_val = [1, board[0]]
	elif board[3] == board[4] == board[5] and board[3] in [player1, player2]:	returned_val = [1, board[3]]
	elif board[6] == board[7] == board[8] and board[6] in [player1, player2]:	returned_val = [1, board[6]]
	elif board[0] == board[3] == board[6] and board[0] in [player1, player2]:	returned_val = [1, board[0]]
	elif board[1] == board[4] == board[7] and board[1] in [player1, player2]:	returned_val = [1, board[1]]
	elif board[2] == board[5] == board[8] and board[2] in [player1, player2]:	returned_val = [1, board[2]]
	elif board[0] == board[4] == board[8] and board[0] in [player1, player2]:	returned_val = [1, board[0]]
	elif board[2] == board[4] == board[6] and board[2] in [player1, player2]:	returned_val = [1, board[2]]
	elif '-' in board:	returned_val = [0, board[0]]
	else:	returned_val = [2, board[0]]
	return returned_val

def move_random(moves_list):
	"""
	returns random index of one of the many possible moves
	"""
	return random.choice(moves_list)

def the_move(board, lst):
	"""
	returns a random index out of the best moves
	"""
	max_val = max(lst)
	max_array = []
	for i in range(len(lst)):
		if lst[i] == max_val:
			max_array.append(i)
	k = move_random(max_array)
	cntr = 0
	for i in range(9):
		if board[i] == '-':
			cntr += 1
		if cntr == k+1:
			return i
