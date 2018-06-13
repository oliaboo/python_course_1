
class Rectangle:

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def compute_area(self):
		return self.length * self.width


r = Rectangle(4, 6)
r.compute_area()
