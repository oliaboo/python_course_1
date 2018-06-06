while True:
	a = input('Enter A: ')
	if a == 'q':
		break
	
	b = input('Enter B: ')
	if b == 'q':
		break
	
	op = input('Enter operation: ')
	if op == 'q':
		break
	
	try:
		int(a)
		int(b)
	except ValueError:
		print('value is not integer')
		continue
	else:
		a = int(a)
		b = int(b)

	if op == '+':
		print('a + b =', a + b)
	elif op == '-':
		print('a - b =', a - b)
	elif op == '/':
		print('a / b =', a/b)
	elif op == '%':
		print('a % b =', a%b)
	elif op == '**':
		print('a ** b =', a**b)
	else:
		print("You've entered unknown oprtation")


