from __future__ import print_function

import random
import sys
from optparse import OptionParser

def get_options():
	parser = OptionParser()
	parser.add_option('-s', '--sides', default=6, type="int")
	options, args = parser.parse_args()
	try:
		number = int(args.pop())
	except:
		number = 1
	options.number = number
	return options

class Dice(object):
	def __init__(self, sides):
		self.sides = sides

	def roll(self):
		return random.randint(1, self.sides)

def do_dice_roll():
	"""
	Roll n-sided dice and return each result and the total
	"""
	options = get_options()
	dice = Dice(options.sides)
	rolls = [dice.roll() for n in range(options.number)]
	for roll in rolls:
		print('rolled', roll)
	if options.number > 1:
		print('total', sum(rolls))
