op_list = ["-","+","/","*","**"]
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
        res = number1 - number2
    elif operand == "+":
        res = number1 + number2
    elif operand == "/":
        try:
            res = number1 / number2
        except ZeroDivisionError:
            print('Infinity')
            continue
    elif operand == "*":
        res = number1 * number2
    elif operand == "%":
        res = number1 % number2
    elif operand == "**":
        res = number1 ** number2
    print(res)
    
