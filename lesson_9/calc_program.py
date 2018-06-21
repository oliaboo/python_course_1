from calculator.calculator import Calculator
import csv

open('history.csv', 'w').close()

print('Write an expression in one line. ex.: A*B')

print('\nIf you want to quit write an exit')

while True:

    raw_expression = input('\nExpression: ')

    raw_expression = raw_expression.replace(' ', '')                                                                    # remove all spaces

    if raw_expression == 'exit':

        break

    if raw_expression == 'history':

        print('\n')

        with open('history.csv', 'r') as f:

            reader = csv.reader(f, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

            for row in reader:

                if row != []:

                    print(row[0], row[1], row[2], row[3])

        continue

    expression_length = len(raw_expression)

    if expression_length >= 3:                                                                                          # checking for the minimum line size

        Calculator.calculation(raw_expression)
        
    else:

        print('\nExpression Error!')

        continue
