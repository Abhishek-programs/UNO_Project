from time import sleep
from collections import deque
from players import Players
import os


class Game:
	def __init__(self, player1: Players, player2: Players, player3: Players, player4: Players, pull_deck, discard):
		self.player1 = player1
		self.player2 = player2
		self.player3 = player3
		self.player4 = player4
		self.pull_deck = pull_deck
		self.previous_card = discard
		self.discard_deck = [self.previous_card]
		self.players = deque([self.player1, self.player2, self.player3, self.player4])
		self.turn = "clock"
		self.skipped = False

	def play(self):
		print("Start the Game")
		while not self.win():
			if not self.skipped:
				if self.previous_card.ability == "Reverse":
					self.reverse()
				next_player = self.next_player()
				if self.previous_card.ability == "Skip":
					next_player = self.next_player()
				if self.previous_card.ability == "+2":
					next_player.pull_card(self.pull_deck)
					next_player.pull_card(self.pull_deck)
					next_player = self.next_player()
				if self.previous_card.ability == "+4":
					next_player.pull_card(self.pull_deck)
					next_player.pull_card(self.pull_deck)
					next_player.pull_card(self.pull_deck)
					next_player.pull_card(self.pull_deck)
					next_player = self.next_player()
			else:
				next_player = self.next_player()
				self.skipped = False
			self.start_the_game(next_player)
		print("Game Over")

	def start_the_game(self, players):
		players.print_cards(self.previous_card)
		self.previous_card, self.pull_deck, self.skipped = players.start(self.previous_card, self.pull_deck)
		self.discard_deck.append(self.previous_card)
		players.print_cards(self.previous_card)
		sleep(3)
		clearConsole()

	def next_player(self):
		if self.turn == "clock":
			self.players.rotate(-1)
			return self.players[-1]
		else:
			self.players.rotate(1)
			return self.players[-1]

	def reverse(self):
		if self.turn == "clock":
			self.turn = "counter"
		else:
			self.turn = "clock"

	def win(self):
		if len(self.player1.cards) == 0:
			print("Player 1 wins")
			return True
		elif len(self.player2.cards) == 0:
			print("Player 2 wins")
			return True
		elif len(self.player3.cards) == 0:
			print("Player 3 wins")
			return True
		elif len(self.player4.cards) == 0:
			print("Player 4 wins")
			return True
		else:
			return False


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
