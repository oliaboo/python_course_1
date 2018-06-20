class SomeClass:
	
	user_string = ""

	def get_String(self):
		self.user_string = input('enter a string: ')

	def print_String(self):
		return self.user_string.upper()

sc = SomeClass()
sc.get_String()
print(sc.print_String())