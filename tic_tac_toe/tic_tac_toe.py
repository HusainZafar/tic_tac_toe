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
	parser = argparse.ArgumentParser(description=	'Play a game of Tic Tac Toe')
	parser.add_argument('--mode', type=str, default = 's', choices = ['s', 't'], help = 'Mode: s(single player):default, t(two-player)')	
	mode = parser.parse_args().mode
	utils.clearScreen()
	game = tic_tac_toe(mode)
	#549946 iterarions minimax
	#upper limit 1+9*(1+8*(...(1+2*(1+1)...))

class tic_tac_toe:
	def __init__(self, mode):
		board = constants.board
		if mode == 's':
			self.one_player(board)
		elif mode == 't':
			self.two_player(board)

	def minimax(self, board, move, computerChar, playerChar, depth=0):
		"""
		Implements the minimax algorithm. Returns 1 : computer has won.
		Returns -1 when player wins.
		When it's the computer's turn and it has to return a value to its parent,
		the maximum value from the array is chosen else, the minimum value.
		"""
		[is_win, who_won] = utils.check_win(board, computerChar, playerChar)
		if is_win == 2:			   
			return 0
		if is_win == 1:
			if who_won == computerChar:
				return 1
			if who_won == playerChar:
				return -1
		ret_list = []
		for i in range(9):
			if board[i] == '-':
				if move == computerChar:
					next_move = playerChar
				else:
					next_move = computerChar
				board[i] = move
				minimax_val = self.minimax(board, next_move, computerChar, playerChar, depth + 1)
				board[i] = '-'
				ret_list.append(minimax_val)
		if depth == 0:
			return ret_list
		if move == computerChar:
			return max(ret_list)
		else:
			return min(ret_list)

	def one_player(self, board):
		"""
		Play with the computer
		"""
		keyboardIndexMapping = constants.keyboardIndexMapping
		computerChar, playerChar, displayWinChance, whichPlayerFirst = utils.getSinglePlayerDetails()
	
		if whichPlayerFirst == 1:
			utils.clearScreen()
			utils.display_board(board)
			while utils.check_win(board, computerChar, playerChar)[0] == 0:
				if utils.check_empty(board):
					tut = [0,0,0,0,0,0,0,0,0]
				else:
					tut = [-i for i in self.minimax(board, playerChar, computerChar, playerChar)]
				if displayWinChance == 1:
					utils.clearScreen()
					utils.display_tutorial_board(board, tut)
				index = int(input())
				if index > 9 or index < 1:
					utils.clearScreen()
					utils.display_board(board)
					if displayWinChance == 1:
						utils.clearScreen()
						utils.display_tutorial_board(board, tut)
					continue
				index = keyboardIndexMapping[index]
				# cant use already used index
				if board[index] != '-':
					utils.clearScreen()
					utils.display_board(board)
					if displayWinChance == 1:
						utils.clearScreen()
						utils.display_tutorial_board(board, tut)
					continue
				board[index] = playerChar
				utils.clearScreen()
				utils.display_board(board)
				if displayWinChance == 1:
					utils.clearScreen()
					utils.display_tutorial_board(board, tut)
				if utils.check_win(board, computerChar, playerChar)[0] != 0:
					break
				ret = self.minimax(board, computerChar, computerChar, playerChar)
				# chose move for computer
				board[utils.the_move(board, ret)] = computerChar
				utils.clearScreen()
				utils.display_board(board)
			if utils.check_win(board, computerChar, playerChar)[0] == 1:
				print ("You lost!!")
			else:
				print ("It's a draw!")
	
		if whichPlayerFirst == 2:
			while utils.check_win(board, computerChar, playerChar)[0] == 0:
				if utils.check_empty(board):
					board[random.randrange(0,9)] = computerChar
				else:
					ret = self.minimax(board, computerChar, computerChar, playerChar)
					# chose move for computer
					board[utils.the_move(board, ret)] = computerChar
				utils.clearScreen()
				utils.display_board(board)
				if utils.check_win(board, computerChar, playerChar)[0] != 0:
						break
				# index already used can't be reused
				flag = 0
				while flag == 0:
					tut = [-i for i in self.minimax(board, playerChar, computerChar, playerChar)]
					utils.clearScreen()
					utils.display_board(board)
					if displayWinChance == 1:
						utils.clearScreen()
						utils.display_tutorial_board(board, tut)
					index = int(input())
					if index > 9 or index < 1:
						utils.clearScreen()
						utils.display_board(board)
						if displayWinChance == 1:
							utils.clearScreen()
							utils.display_tutorial_board(board, tut)
						continue
					index = keyboardIndexMapping[index]
					if board[index] == '-':
						flag = 1
						board[index] = playerChar
						utils.clearScreen()
						utils.display_board(board)
						if displayWinChance == 1:
							utils.clearScreen()
							utils.display_tutorial_board(board, tut)
					else:
						utils.clearScreen()
						utils.display_board(board)
						if displayWinChance == 1:
							utils.clearScreen()
							utils.display_tutorial_board(board, tut)
	
			if utils.check_win(board, computerChar, playerChar)[0] == 1:
				print ("You lost!!")
			else:
				print ("It's a draw!")

	def two_player(self, board):
		'''
		Play in 2 player mode
		'''
		keyboardIndexMapping = constants.keyboardIndexMapping
		playerOne, playerTwo, playerOneChar, playerTwoChar, whichPlayerFirst = utils.getTwoPlayerDetails()
		move_mapping = {playerOne:playerOneChar, playerTwo:playerTwoChar}

		if whichPlayerFirst == 1:
			chance = playerOne
		else:
			chance = playerTwo
	
		while(utils.check_win(board, playerOneChar, playerTwoChar)[0] == 0):
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
			if(chance==playerOne):
				chance = playerTwo
			else:
				chance = playerOne
		[isWin, whoWon] = utils.check_win(board, playerOneChar, playerTwoChar)
		if(isWin==2):
			utils.clearScreen()
			utils.display_board(board)
			print ("It's a tie")
		if(isWin==1):
			utils.clearScreen()
			utils.display_board(board)
			if(whoWon == playerOneChar):
				print(playerOne + " won!")
			else:
				print(playerTwo + " won!")
	
if __name__ == "__main__":
	main()
