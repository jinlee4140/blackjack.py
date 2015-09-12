class card:
	def init(self, value, suit):
		self.value = value
		self.suit = suit
		if value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
			self.value = int(value)
		if value in ['J', 'Q', 'K']:
			self.value = 10
		if value == 'A'
			self.value = 1
		