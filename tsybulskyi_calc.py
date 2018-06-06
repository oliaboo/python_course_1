
def operations(a, b, op):
	"""function requires 3 paramters:
	a - first operand, integre only
	b - second operand, integer only
	op - operation, shall be one of '+', '-', '/', '%', '**' """

	if op == '+':
		print('a + b =', a + b)
	elif op == '-':
		print('a - b =', a - b)
	elif op == '/':
		try:
			print('a / b =', a/b)
		except ZeroDivisionError:
			print('Cannot devide by zero')
	elif op == '%':
		try:
			print('a % b =', a%b)
		except ZeroDivisionError:
			print('Cannot devide by zero')
	elif op == '**':
		print('a ** b =', a**b)
	else:
		print("You've entered unknown oprtation")


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
	elif op not in ['+', '-', '/', '%', '**']:
		print('Unsupported opperation')
		continue

	operations(a, b, op)