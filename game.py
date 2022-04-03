# class Deck:
#     def __init__(self, pull, discard):
#         self.pull = pull
#         self.discard = discard
#
#     def discard_card(self, number):
#         card = self.cards[number]
#         Players.remove_card(card)
#         self.discard.append(card)
#
#     def pull_card(self):
#         card = self.pull.pop()
#         Players.add_card(card)
from time import sleep

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

	def play(self):
		print("Start the Game")
		while self.win():
			for _ in [self.player1, self.player2, self.player3, self.player4]:
				self.start_the_game(_)
		print("Game Over")

	def start_the_game(self, players):
		players.print_cards(self.previous_card)
		self.previous_card, self.pull_deck = players.start(self.previous_card, self.pull_deck)
		self.discard_deck.append(self.previous_card)
		players.print_cards(self.previous_card)
		sleep(3)
		clearConsole()

	def win(self):
		if len(self.player1.cards) == 0:
			print("Player 1 wins")
			return False
		elif len(self.player2.cards) == 0:
			print("Player 2 wins")
			return False
		elif len(self.player3.cards) == 0:
			print("Player 3 wins")
			return False
		elif len(self.player4.cards) == 0:
			print("Player 4 wins")
			return False
		else:
			return True
	# print(self.previous_card.display_card())
	# for _ in self.discard_deck:
	# 	print(_.display_card())


# for _ in self.pull_deck:
# 	print(_.display_card())


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
