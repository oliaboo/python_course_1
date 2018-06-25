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

    return x / y
	    


def calculation(raw_expression): 

    operations = {'/': divide, '*': multiply, '+': add, '-': subtract}

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

                    return result

                else:

                    return result

                break


            else:

                print('\nExpression Error!')

                break

    print('\nExpression Error!')

def main(): 

    print('Write an expression in one line. ex.: A*B')

    print('\nIf you want to quit write an exit')

    while True:

        raw_expression = input('\nExpression: ')

        raw_expression = raw_expression.replace(' ', '')                                                                                     # remove all spaces

        if raw_expression == 'exit':

            break

        expression_length = len(raw_expression)

        if expression_length >= 3:                                                                                          # checking for the minimum line size

            result = calculation(raw_expression)

            print(result)
            
        else:

            print('\nExpression Error!')

            continue

if __name__ == "__main__":

    main()

