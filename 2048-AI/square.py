import random

class Square(object):
	""" 
	Describes a single 'tile' in a game of 2048
	Contains a single property, 'value', which represents its numeric value
	"""

	def __init__(self):
		self.value = 0		

	def set_random_value(self):
		"""
		Set this square to have a value of either two or four
		"""
		self.value = 2 if random.random() < 0.9 else 4		

