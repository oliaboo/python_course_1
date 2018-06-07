class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This method adds two numbers 
    def add(self):
        return self.x + self.y

    # This method subtracts two numbers 
    def subtract(self):
        return self.x - self.y

    # This method multiplies two numbers
    def multiply(self):
        return self.x * self.y

    # This method divides two numbers
    def divide(self):
            try:
                    self.x / self.y
            except ZeroDivisionError:
                    return 'Division by zero'
            return self.x / self.y
        
    # This method makes calculations
    def calculation(raw_expression): 

        operations = {'/': Calculator.divide, '*': Calculator.multiply, '+': Calculator.add, '-': Calculator.subtract}

        for operation in operations:

            if operation in raw_expression:                                                                             # checking for an operation in a string    

                operation_index = raw_expression.index(operation)

                if operation_index > 0 and operation_index < len(raw_expression):                                       # checking for an operation place in a string

                    if raw_expression[0:operation_index].isdigit():
        
                        x = float(raw_expression[0:operation_index])

                    else:

                        break

                    if raw_expression[operation_index+1:expression_length].isdigit():

                        y = float(raw_expression[operation_index+1:expression_length])
                        
                    else:

                        break
                        
                    Calc = Calculator(x, y)

                    result = operations[operation](Calc)

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


print('Write an expression in one line. ex.: A*B')

print('\nIf you want to quit write an exit')

while True:

    raw_expression = input('\nExpression: ')

    raw_expression.replace(' ', '')                                                                                     # remove all spaces

    if raw_expression == 'exit':

        break

    expression_length = len(raw_expression)

    if expression_length >= 3:                                                                                          # checking for the minimum line size

        Calculator.calculation(raw_expression)
        
    else:

        print('\nExpression Error!')

        continue


