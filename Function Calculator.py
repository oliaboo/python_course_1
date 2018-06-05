# This function adds two numbers 

def add(x, y):

    return x + y

# This function subtracts two numbers 

def subtract(x, y):

    return x - y

# This function multiplies two numbers

def multiply(x, y):

    return x * y

# This function divides two numbers

def divide(x, y):

	try:
		
		x / y

	except ZeroDivisionError:

		return 'Division by zero'
	    
	return x / y

operations = {'/': divide, '*': multiply, '+': add, '-': subtract}

counter = 0 

print('Write an expression in one line. ex.: A*B')

print('\nIf you want to quit write an exit')

while True:

    raw_expression = input('\nExpression: ')

    raw_expression.replace(' ', '')                                                                                     # remove all spaces

    if raw_expression == 'exit':

        break

    expression_length = len(raw_expression)

    if expression_length >= 3:                                                                                          # checking for the minimum line size

        for operation in operations:

            if operation in raw_expression:                                                                             # checking for an operation in a string    

                operation_index = raw_expression.index(operation)

                if operation_index > 0 and operation_index < len(raw_expression):                                       # checking for an operation place in a string

                    x = float(raw_expression[0:operation_index])

                    y = float(raw_expression[operation_index+1:expression_length])

                    result = operations[operation](x, y)

                    print('\n')

                    if type(result) is float:

                        print("Result : ", "%.2f" % result, '\n')

                    else:

                        print(result, '\n')

                    break


                else:

                    print('\nExpression Error!')

                    break

            else:

                counter = counter + 1

                if counter == 4:

                    counter = 0

                    print('\nExpression Error!')

                    break

    else:

        print('\nExpression Error!')

        continue


