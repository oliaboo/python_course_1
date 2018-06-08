class Calculator:
    def subtraction(self):
        """Subtracts number2  from number1"""
        return number1-number2

    def addition(self):
        """Adds values of number1 and number2"""
        return number1+number2

    def division(self):
        """Divides number1 by number2"""
        try:
            return number1/number2
        except ZeroDivisionError:
                return 'Infinity'
        
    def multiplication(self):
        """Multiplies values of number1 and number2"""
        return number1*number

    def modulus(self):
        """Divides number1 by number2 and returns remainder"""
        return number1%number2

    def exponentiation(self):
        """Performs exponential calculation of number1 to the power number2"""
        return number1**number2
        
    
op_list = ["-","+","/","*","**","%"]
    
while True:
    calc = Calculator()
    number1 = input("Enter your first number ")
    if number1 == 'exit':
        break
    try:
        number1 = float(number1)
    except ValueError:
        print("Wrong value of first number")
        continue
    operand = input("Enter the operand ")
    if operand in op_list:
        pass
    else:
        print("unknown operand")
        continue
    number2 = input("Enter your second number ")
    if number2 == 'exit':
        break
    try:
        number2 = float(number2)
    except ValueError:
        print("Wrong value of second number")
        continue
        
    if operand == "-":
        print(calc.subtraction())
    elif operand == "+":
        print(calc.addition())
    elif operand == "/":
        print(calc.division())
    elif operand == "*":
        print(calc.multiplication())
    elif operand == "%":
        print(calc.modulus())
    elif operand == "**":
        print(calc.exponentiation())    
