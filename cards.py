from termcolor import colored


class Cards:
	def __init__(self, number=None, color="grey", ability=None):
		self.number = number
		self.color = color
		self.ability = ability

	def __repr__(self):
		return f"{self.number} {self.color} {self.ability}"

	def display_card(self):
		if self.ability:
			return colored(self.ability, self.color)
		else:
			return colored(self.number, self.color)
