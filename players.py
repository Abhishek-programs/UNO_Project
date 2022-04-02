class Players:
	def __init__(self, name, cards):
		self.name = name
		self.cards = cards

	def __repr__(self):
		return f"{self.name}: {self.cards}"

	def print_cards(self, previous):
		print(f"The previous card {previous.display_card()}")
		print(f"{self.name} Cards")
		for card in self.cards:
			print(card.display_card())

	def start(self, previous_card):
		if self.card_exists(previous_card):
			return self.play_card(previous_card)
		else:
			self.pull_card()

	def play_card(self, previous_card):
		card_no = int(input("Type card you want to play"))
		if input("Are you sure?: y/n") in ["Y", "y"]:
			try:
				card = self.cards[card_no - 1]
			except IndexError:
				print("Out of Range")
				return self.play_card(previous_card)
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
					return self.play_card(previous_card)

	@staticmethod
	def check_valid(card, previous):
		if card.ability in ["+4", "Wild"]:
			return True
		if (card.number == previous.number and card.number is not None) or (
				card.color == previous.color and card.color is not None) or (
				card.ability == previous.ability and card.ability is not None):
			return True
		return False

	def card_exists(self, previous_card):
		pass

	def pull_card(self):
		pass
