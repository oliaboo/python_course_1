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

def calculation(raw_expression): 

    for operation in operations:

        if operation in raw_expression:                                                                             # checking for an operation in a string    

            operation_index = raw_expression.index(operation)

            if operation_index > 0 and operation_index < len(raw_expression):                                       # checking for an operation place in a string

                if raw_expression[0:operation_index].isdigit():
    
                    x = float(raw_expression[0:operation_index])

                else:

                    break

                if raw_expression[operation_index+1:].isdigit():

                    y = float(raw_expression[operation_index+1:])
                    
                else:

                    break

                result = operations[operation](x, y)

                print('\n')

                if type(result) is float:

                    return print("Result : ", "%.2f" % result, '\n')

                else:

                    return print(result, '\n')

                break


            else:

                print('\nExpression Error!')

                break

    print('\nExpression Error!')


operations = {'/': divide, '*': multiply, '+': add, '-': subtract} 

print('Write an expression in one line. ex.: A*B')

print('\nIf you want to quit write an exit')

while True:

    raw_expression = input('\nExpression: ')

    raw_expression = raw_expression.replace(' ', '')                                                                                     # remove all spaces

    if raw_expression == 'exit':

        break

    expression_length = len(raw_expression)

    if expression_length >= 3:                                                                                          # checking for the minimum line size

        calculation(raw_expression)
        
    else:

        print('\nExpression Error!')

        continue
