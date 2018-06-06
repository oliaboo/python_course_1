
class Calculator:

	def __init__(self, a, b, op):
		self.a = a
		self.b = b
		self.op = op

	def add(self):
		return self.a + self.b

	def minus(self):
		return self.a - self.b

	def divide(self):
		try:
			self.a / self.b
		except ZeroDivisionError:
			return 0
		else:
			return self.a / self.b

	def divide_by_module(self):
		try:
			self.a % self.b
		except ZeroDivisionError:
			return 0
		else:
			return self.a % self.b

	def check_operation(self):
		if op not in ['+', '-', '/', '%']:
			return False
		else:
			return True

	def calculate(self):
		if self.check_operation():
			if op == '+':
				return self.add()
			elif op == '-':
				return self.minus()
			elif op == '/':
				return self.divide()
			elif op == '%':
				return self.divide_by_module()
		else:
			return False


while True:
	a = input('Enter A: ')
	if a == 'q':
		break
	else:
		try:
			a = int(a)
		except ValueError:
			print('value is not integer')
			continue

	b = input('Enter B: ')
	if b == 'q':
		break
	else:
		try:
			b = int(b)
		except ValueError:
			print('value is not integer')
			continue

	op = input('Enter operation: ')
	if op == 'q':
		break

	calc = Calculator(a, b, op)
	print(calc.calculate())
