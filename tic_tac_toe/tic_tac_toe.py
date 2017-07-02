"""
Tic Tac Toe
Author: Husain Zafar
Provides an elegant playing experience
Uses Minimax algorithm
Single and Two player modes
Includes an option to display chances of winning per playable box, per move. 
"""
import random
import argparse
import sys
import os
from builtins import input

def main(args=None):
	board =['-', '-', '-',
		'-', '-', '-',
		'-', '-', '-']
	COUNT = 0
	parser = argparse.ArgumentParser(description=	'Play a game of Tic Tac Toe')
	parser.add_argument('--mode', type=str, default = 's', choices = ['s', 't'], help = 'Mode of play: s(single) or t(two-player) (default: s)')	
	args = parser.parse_args()
	if args.mode == 's':
		_ = os.system('clear')
		one_player(board)
	elif args.mode == 't':
		_ = os.system('clear')
		two_player(board)
	#549946 iterarions minimax
	#upper limit 1+9*(1+8*(...(1+2*(1+1)...))

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
	while j < len(board) :
		if board[j] == '-':
			if tut[i] == 1:
				prob[j] = 'W'
			if tut[i] == 0:
				prob[j] = 'D'
			if tut[i] ==-1:
				prob[j] = 'L'
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
	for i in range(0,9):
		if board[i] != '-':
			return False
	return True
	
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
	import random
	random = random.randrange(0, len(moves_list))
	return moves_list[random]

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

def minimax(board, move, comp, plr):
	"""
	Implements the minimax algorithm. Returns 1 : computer has won.
	Returns -1 when player wins.
	When it's the computer's turn and it has to return a value to its parent,
	the maximum value from the array is chosen else, the minimum value.
	"""
	global COUNT
	COUNT += 1
	[is_win, who_won] = check_win(board, comp, plr)
	if is_win == 2:			   
		return 0
	if is_win == 1:
		if who_won == comp:
			return 1
		if who_won == plr:
			return -1
	ret_list = []
	for i in range(9):
		if board[i] == '-':
			if move == comp:
				next_move = plr
			else:
				next_move = comp
			board[i] = move
			minimax_val = minimax(board, next_move, comp, plr)
			board[i] = '-'
			ret_list.append(minimax_val)
			COUNT -= 1
	if COUNT <= 1:
		return ret_list
	if move == comp:
		return max(ret_list)
	else:
		return min(ret_list)

def one_player(board):
	"""
	Play with the computer
	"""
	index_mapping = {7:0,8:1,9:2,4:3,5:4,6:5,1:6,2:7,3:8}
	order = int(input("first(1) or second(2) ?\n"))
	comp = input("Enter character for computer on board : ")
	plr = input("Enter character for player on board   : ")
	t = input("Display move winning chance? (y/Y)    : ")
	if t == 'Y' or t == 'y':
		t = 1
	else:
		t = 0

	global COUNT
	if order == 1:
		_ = os.system('clear')
		display_board(board)
		while check_win(board, comp, plr)[0] == 0:
			COUNT = 0
			if check_empty(board):
				tut = [0,0,0,0,0,0,0,0,0]
			else:
				tut = [-i for i in minimax(board, plr, comp, plr)]
			if t == 1:
				_ = os.system('clear')
				display_tutorial_board(board, tut)
			index = int(input())
			if index > 9 or index < 1:
				_ = os.system('clear')
				display_board(board)
				if t == 1:
					_ = os.system('clear')
					display_tutorial_board(board, tut)
				continue
			index = index_mapping[index]
			# cant use already used index
			if board[index] != '-':
				_ = os.system('clear')
				display_board(board)
				if t == 1:
					_ = os.system('clear')
					display_tutorial_board(board, tut)
				continue
			board[index] = plr
			_ = os.system('clear')
			display_board(board)
			if t == 1:
				_ = os.system('clear')
				display_tutorial_board(board, tut)
			COUNT = 0
			if check_win(board, comp, plr)[0] != 0:
				break
			ret = minimax(board, comp, comp, plr)
			# chose move for computer
			board[the_move(board, ret)] = comp
			_ = os.system('clear')
			display_board(board)
		if check_win(board, comp, plr)[0] == 1:
			print ("You lost!!")
		else:
			print ("It's a draw!")

	if order == 2:
		while check_win(board, comp, plr)[0] == 0:
			COUNT = 0
			if check_empty(board):
				board[random.randrange(0,9)] = comp
			else:
				ret = minimax(board, comp, comp, plr)
				# chose move for computer
				board[the_move(board, ret)] = comp
			_ = os.system('clear')
			display_board(board)
			if check_win(board, comp, plr)[0] != 0:
					break
			# index already used can't be reused
			flag = 0
			while flag == 0:
				COUNT = 0
				tut = [-i for i in minimax(board, plr, comp, plr)]
				_ = os.system('clear')
				display_board(board)
				if t == 1:
					_ = os.system('clear')
					display_tutorial_board(board, tut)
				index = int(input())
				if index > 9 or index < 1:
					_ = os.system('clear')
					display_board(board)
					if t == 1:
						_ = os.system('clear')
						display_tutorial_board(board, tut)
					continue
				index = index_mapping[index]
				if board[index] == '-':
					flag = 1
					board[index] = plr
					_ = os.system('clear')
					display_board(board)
					if t == 1:
						_ = os.system('clear')
						display_tutorial_board(board, tut)
				else:
					_ = os.system('clear')
					display_board(board)
					if t == 1:
						_ = os.system('clear')
						display_tutorial_board(board, tut)

		if check_win(board, comp, plr)[0] == 1:
			print ("You lost!!")
		else:
			print ("It's a draw!")

def two_player(board):
	'''
	Play in 2 player mode
	'''
	index_mapping = {7:0,8:1,9:2,4:3,5:4,6:5,1:6,2:7,3:8}
	player1 = input("Player 1 name (Player 1): ")
	player2 = input("Player 2 name (Player 2): ")
	if player1 == '':
		player1 = 'Player1'
	if player2 == '':
		player2 = 'Player2'
	plr1 = input("Enter character for "+ player1 + " on board (x): ")

	if plr1 == '':
		plr1 = 'x'
	plr2 = input("Enter character for "+ player2 + " on board (o): ")	
	if plr2 == '':
		plr2 = 'o'
	
	move_mapping = {player1:plr1, player2:plr2}
	m = input("Who goes first, " + player1 + " or " + player2 + " (1/2)? (1): ")
	if m == '':
		m = 1
	m = int(m)
	if m == 1:
		chance = player1
	else:
		chance = player2	
	while(check_win(board, plr1, plr2)[0] == 0):
		_ = os.system('clear')
		display_board(board)
		print(chance + ": Your chance")
		index = int(input())
		if index > 9 or index < 1:
			_ = os.system('clear')
			continue		
		index = index_mapping[index]
		if(board[index] != '-'):
			continue
		board[index] = move_mapping[chance]
		if(chance==player1):
			chance = player2
		else:
			chance = player1
	[a,b] = check_win(board, plr1, plr2)
	if(a==2):
		_ = os.system('clear')
		display_board(board)
		print ("It's a tie")
	if(a==1):
		_ = os.system('clear')
		display_board(board)
		if(b == plr1):
			print(player1 + " won!")
		else:
			print(player2 + " won!")

if __name__ == "__main__":
	main()
