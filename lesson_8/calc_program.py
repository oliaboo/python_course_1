from calculator.calculator import Calculator

print('Write an expression in one line. ex.: A*B')

print('\nIf you want to quit write an exit')

while True:

    raw_expression = input('\nExpression: ')

    raw_expression = raw_expression.replace(' ', '')                                                                    # remove all spaces

    if raw_expression == 'exit':

        break

    expression_length = len(raw_expression)

    if expression_length >= 3:                                                                                          # checking for the minimum line size

        Calculator.calculation(raw_expression)
        
    else:

        print('\nExpression Error!')

        continue
