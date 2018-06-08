op_list = ["-","+","/","*","**","%"]

def subtraction():
    """Subtracts number2  from number1"""
    return number1-number2

def addition():
    """Adds values of number1 and number2"""
    return number1+number2

def division():
    """Divides number1 by number2"""
    try:
        return number1/number2
    except ZeroDivisionError:
            return 'Infinity'
        
def multiplication():
    """Multiplies values of number1 and number2"""
    return number1*number

def modulus():
    """Divides number1 by number2 and returns remainder"""
    return number1%number2

def exponentiation():
    """Performs exponential calculation of number1 to the power number2"""
    return number1**number2
    
    
while True:
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
        print(subtraction())
    elif operand == "+":
        print(addition())
    elif operand == "/":
        print(division())
    elif operand == "*":
        print(multiplication())
    elif operand == "%":
        print(modulus())
    elif operand == "**":
        print(exponentiation())
