a_end = '0'

while a_end != 'exit':

	#input and check first argument:

	while True:
		try:
			a_first = int(input('pls input your first argument: \n'))
			break
		except:
			print('Wrong data type! \n')

	#input and check second argument, operation symbol and performing operation:

	while True:
		try:
			a_second = int(input('\npls input your second argument: \n'))
		except:
			print('Wrong data type! \n')

		#input and check operation symbol

		while True:
				operation = input('choose math operation: +, -, /, *, %, ** \n')
				if operation =='+' or operation =='-' or operation =='/' or operation =='*' or operation =='%' or operation =='**':
					break
			break
				else:
					print('Wrong data type! \n')

		#performing operation

	try:
		if operation == '+':
			print('your result: ', float(a_first)+float(a_second))
			break
		elif operation == '-':
			print('your result: ', float(a_first)-float(a_second))
			break
		elif operation == '/':
			print('your result: ', float(a_first)/float(a_second))
			break
		elif operation == '*':
			print('your result: ', float(a_first)*float(a_second))
			break
		elif operation == '**':
			print('your result: ', float(a_first)**float(a_second))
			break
		elif operation == '%':
			print('your result: ', float(a_first)%float(a_second))
			break
	except: 
		print('\nCan`t devide by zero')
	a_end =input('Type \'exit\' if you want to exit calculator or press \'Enter\':')

