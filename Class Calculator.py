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
        

operations = {'/': Calculator.divide, '*': Calculator.multiply, '+': Calculator.add, '-': Calculator.subtract} 

print('Write an expression in one line. ex.: A*B')

print('\nIf you want to quit write an exit')

while True:

    counter = 0

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

                    Calc = Calculator(x, y)

                    result = operations[operation](Calc)

                    print('\n')

                    if type(result) is float:

                        print("Result : ", "%.2f" % result, '\n')

                    else:

                        print(result, '\n')

                    break


                else:

                    print('\nExpression Error 1 !')

                    break

            else:

                counter = counter + 1

                if counter == 4:

                    counter = 0

                    print('\nExpression Error 2!')

                    break

    else:

        print('\nExpression Error 3!')

        continue


