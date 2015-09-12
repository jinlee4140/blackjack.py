class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		if value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
			self.value = int(value)
		if value in ['J', 'Q', 'K']:
			self.value = 10
		if value == 'A':
			self.value = 1

	def val(self):
		return self.value

	def selfsuit(self):
		return self.suit



james = Card(10, 'heart')
print james.val()
print james.selfsuit()
#unfinished work