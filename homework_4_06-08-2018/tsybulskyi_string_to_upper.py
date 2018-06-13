
class StringToUpper:

	def get_String(self):
		self.str = input('Enter String: ')

	def print_String(self):
		return self.str.upper()

c = StringToUpper()
c.get_String()
c.print_String()