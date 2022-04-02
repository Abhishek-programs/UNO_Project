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
		self.player1.print_cards(self.previous_card)
		self.previous_card = self.player1.play_card(self.previous_card)
		self.discard_deck.append(self.previous_card)
		clearConsole()
		self.player2.print_cards(self.previous_card)
		self.previous_card = self.player2.play_card(self.previous_card)
		self.discard_deck.append(self.previous_card)
		clearConsole()
		self.player3.print_cards(self.previous_card)
		self.previous_card = self.player3.play_card(self.previous_card)
		self.discard_deck.append(self.previous_card)
		clearConsole()
		self.player4.print_cards(self.previous_card)
		self.previous_card = self.player4.play_card(self.previous_card)
		self.discard_deck.append(self.previous_card)
		clearConsole()
		print(self.previous_card.display_card())
		for _ in self.discard_deck:
			print(_.display_card())


# for _ in self.pull_deck:
# 	print(_.display_card())


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
