class Players:
	def __init__(self, name, cards):
		self.name = name
		self.cards = cards

	def __repr__(self):
		return f"{self.name}: {self.cards}"

	def print_cards(self, previous):
		print(f"The previous card {previous.display_card()}")
		print(f"{self.name} Cards")
		for count, card in enumerate(self.cards):
			print(f"{count + 1}. {card.display_card()}")

	def start(self, previous_card, pull_deck):
		option = input("Do You want to Play(p) or Take(t) a Card")
		if option == "p":
			return self.play_card(previous_card, pull_deck), pull_deck
		elif option == "t":
			self.pull_card(pull_deck)
			self.print_cards(previous_card)
			option = input("Skip(s)?")
			if option == 's':
				return previous_card, pull_deck
			else:
				return self.start(previous_card, pull_deck)
		else:
			print("Invalid Option")
			return self.start(previous_card, pull_deck)

	def play_card(self, previous_card, pull_deck):
		try:
			card_no = int(input("Type card you want to play \n press 0 to return"))
		except ValueError:
			print("Enter Number")
			return self.play_card(previous_card, pull_deck)
		if card_no == 0:  # Check If user wants to return
			return self.start(previous_card, pull_deck)[0]
		else:
			_ = input("Are you sure?: y/n")
			if _ in ["Y", "y"]:
				try:
					card = self.cards[card_no - 1]
				except IndexError:
					print("Out of Range")
					return self.play_card(previous_card, pull_deck)
				else:
					if self.check_valid(card, previous_card):
						if card.ability in ["+4", "Wild"]:
							color = int(input("Enter the Color you want to play. 1)Red 2)Green 3)Blue 4)Yellow"))
							card.number = None
							match color:
								case 1:
									card.color = "red"
								case 2:
									card.color = "green"
								case 3:
									card.color = "blue"
								case 4:
									card.color = "yellow"
						return self.cards.pop(card_no - 1)
					else:
						print("Invalid Card")
						return self.play_card(previous_card, pull_deck)
			else:
				return self.play_card(previous_card, pull_deck)

	@staticmethod
	def check_valid(card, previous):
		if card.ability in ["+4", "Wild"]:
			return True
		if (card.number == previous.number and card.number is not None) or (
				card.color == previous.color and card.color is not None) or (
				card.ability == previous.ability and card.ability is not None):
			return True
		return False

	def pull_card(self, pull_deck):
		self.cards.append(pull_deck.pop())  # Pulling card from the deck

