import math

class Circle:

	def __init__(self, radius):
		self.radius = radius

	def compute_area(self):
		return math.pi * self.radius ** 2


	def compute_perimeter(self):
		return 2 * math.pi * self.radius

c = Circle(10)
c.compute_area()
c.compute_perimeter()