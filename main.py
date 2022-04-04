from random import shuffle
from players import Players
from cards import Cards
from game import Game


def create_cards():
	deck = []
	for color in ["red", "blue", "green", "yellow"]:
		for number in range(1, 10):
			deck.append(Cards(number, color, None))
		for ability in ["Skip", "+2", "Reverse"]:
			deck.append(Cards(color=color, ability=ability))

	for special_ability in 2 * ["+4", "Wild"]:
		deck.append(Cards(ability=special_ability))

	return deck


def divide_cards():
	a, b, c, d = [], [], [], []
	cards = create_cards()
	shuffle(cards)
	for _ in range(7):
		a.append(cards.pop(0))
		b.append(cards.pop(0))
		c.append(cards.pop(0))
		d.append(cards.pop(0))

	initial_discard = cards.pop(0)
	while initial_discard.ability in ["+4", "Wild"]:
		cards.append(initial_discard)
		initial_discard = cards.pop(0)

	return a, b, c, d, initial_discard, cards


a, b, c, d, discard, remaining_cards = divide_cards()
player_a = Players("Player1", a)
player_b = Players("Player2", b)
player_c = Players("Player3", c)
player_d = Players("Player4", d)

game = Game(player_a, player_b, player_c, player_d, remaining_cards, discard)
game.play()

# print("Deck Cards:")
# for _ in remaining_cards:
#     print(_.display_card())
