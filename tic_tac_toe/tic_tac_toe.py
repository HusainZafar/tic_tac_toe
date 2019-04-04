"""
Tic Tac Toe
Author: Husain Zafar
Provides an elegant playing experience
Uses Minimax algorithm
Single and Two player modes
Includes an option to display chances of winning per playable box, per move. 
"""

import utils
import random
import argparse
import constants
from builtins import input


def main(args=None):
	board = constants.board
	COUNT = 0
	parser = argparse.ArgumentParser(description=	'Play a game of Tic Tac Toe')
	parser.add_argument('--mode', type=str, default = 's', choices = ['s', 't'], help = 'Mode: s(single player):default, t(two-player)')	
	args = parser.parse_args()
	utils.clearScreen()
	if args.mode == 's':
		one_player(board)
	elif args.mode == 't':
		two_player(board)
	#549946 iterarions minimax
	#upper limit 1+9*(1+8*(...(1+2*(1+1)...))

def minimax(board, move, comp, plr):
	"""
	Implements the minimax algorithm. Returns 1 : computer has won.
	Returns -1 when player wins.
	When it's the computer's turn and it has to return a value to its parent,
	the maximum value from the array is chosen else, the minimum value.
	"""
	global COUNT
	COUNT += 1
	[is_win, who_won] = utils.check_win(board, comp, plr)
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
	keyboardIndexMapping = constants.keyboardIndexMapping
	order = input("first(1) or second(2) ?(Default 1)\n")
	if(order=='1' or order=='2'):
		order = int(order)
	else:
		print("Chosing default 1")
		order = 1
	comp = input("Enter character for computer on board : ")
	plr = input("Enter character for player on board   : ")
	t = input("Display move winning chance? (y/n)    : ")
	if t in ['Y','y']:
		t = 1
	else:
		t = 0

	global COUNT
	if order == 1:
		utils.clearScreen()
		utils.display_board(board)
		while utils.check_win(board, comp, plr)[0] == 0:
			COUNT = 0
			if utils.check_empty(board):
				tut = [0,0,0,0,0,0,0,0,0]
			else:
				tut = [-i for i in minimax(board, plr, comp, plr)]
			if t == 1:
				utils.clearScreen()
				utils.display_tutorial_board(board, tut)
			index = int(input())
			if index > 9 or index < 1:
				utils.clearScreen()
				utils.display_board(board)
				if t == 1:
					utils.clearScreen()
					utils.display_tutorial_board(board, tut)
				continue
			index = keyboardIndexMapping[index]
			# cant use already used index
			if board[index] != '-':
				utils.clearScreen()
				utils.display_board(board)
				if t == 1:
					utils.clearScreen()
					utils.display_tutorial_board(board, tut)
				continue
			board[index] = plr
			utils.clearScreen()
			utils.display_board(board)
			if t == 1:
				utils.clearScreen()
				utils.display_tutorial_board(board, tut)
			COUNT = 0
			if utils.check_win(board, comp, plr)[0] != 0:
				break
			ret = minimax(board, comp, comp, plr)
			# chose move for computer
			board[utils.the_move(board, ret)] = comp
			utils.clearScreen()
			utils.display_board(board)
		if utils.check_win(board, comp, plr)[0] == 1:
			print ("You lost!!")
		else:
			print ("It's a draw!")

	if order == 2:
		while utils.check_win(board, comp, plr)[0] == 0:
			COUNT = 0
			if utils.check_empty(board):
				board[random.randrange(0,9)] = comp
			else:
				ret = minimax(board, comp, comp, plr)
				# chose move for computer
				board[utils.the_move(board, ret)] = comp
			utils.clearScreen()
			utils.display_board(board)
			if utils.check_win(board, comp, plr)[0] != 0:
					break
			# index already used can't be reused
			flag = 0
			while flag == 0:
				COUNT = 0
				tut = [-i for i in minimax(board, plr, comp, plr)]
				utils.clearScreen()
				utils.display_board(board)
				if t == 1:
					utils.clearScreen()
					utils.display_tutorial_board(board, tut)
				index = int(input())
				if index > 9 or index < 1:
					utils.clearScreen()
					utils.display_board(board)
					if t == 1:
						utils.clearScreen()
						utils.display_tutorial_board(board, tut)
					continue
				index = keyboardIndexMapping[index]
				if board[index] == '-':
					flag = 1
					board[index] = plr
					utils.clearScreen()
					utils.display_board(board)
					if t == 1:
						utils.clearScreen()
						utils.display_tutorial_board(board, tut)
				else:
					utils.clearScreen()
					utils.display_board(board)
					if t == 1:
						utils.clearScreen()
						utils.display_tutorial_board(board, tut)

		if utils.check_win(board, comp, plr)[0] == 1:
			print ("You lost!!")
		else:
			print ("It's a draw!")

def two_player(board):
	'''
	Play in 2 player mode
	'''
	keyboardIndexMapping = constants.keyboardIndexMapping
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
	while(utils.check_win(board, plr1, plr2)[0] == 0):
		utils.clearScreen()
		utils.display_board(board)
		print(chance + ": Your chance")
		index = int(input())
		if index > 9 or index < 1:
			utils.clearScreen()
			continue		
		index = keyboardIndexMapping[index]
		if(board[index] != '-'):
			continue
		board[index] = move_mapping[chance]
		if(chance==player1):
			chance = player2
		else:
			chance = player1
	[a,b] = utils.check_win(board, plr1, plr2)
	if(a==2):
		utils.clearScreen()
		utils.display_board(board)
		print ("It's a tie")
	if(a==1):
		utils.clearScreen()
		utils.display_board(board)
		if(b == plr1):
			print(player1 + " won!")
		else:
			print(player2 + " won!")

if __name__ == "__main__":
	main()
