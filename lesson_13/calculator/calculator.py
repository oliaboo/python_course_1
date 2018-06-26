from calculator.operations import operations
import csv

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
        
    def history(x, y, operation, result):
        with open('history.csv', 'a') as f:
            line = [[x, y, operation, result]]
            writer = csv.writer(f)
            writer.writerows(line)
        
    # This method makes calculations
    def calculation(x, y, operation):
        Calc = Calculator(x, y)
        result = eval(operations[operation])(Calc)
        Calculator.history(x, y, operation, result)
        return result
