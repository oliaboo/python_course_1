class Calculator:
    def __init__(self,number1=None,operand=None,number2=None):
        self.number1 = number1
        self.operand = operand
        self.number2 = number2

    def set_numbers(self):
        if self.number1 == None:
            self.number1 = input('Enter first number ')
        else:
            self.number2 = input('Enter second number ')

    def set_operand(self):
        self.operand = input('Enter operand ')
        

    def check(self):
        if self.number1 == 'exit' or self.number2 == 'exit':
            return False
        else:
            return True

    def operand_check(self):
        if self.operand not in op_list:
            print('unknown operand')
            return False
        else:
            return  True
    def first_float(self):
        try:
            self.number1 = float(self.number1)
            return True
        except ValueError:
            print("Wrong value of first number")
            return False
    def second_float(self):
        try:
            self.number2 = float(self.number2)
            return True
        except ValueError:
            print("Wrong value of second number")
            return False
    def start(self):
        if self.operand == "-":
            return self.subtraction()
        elif self.operand == "+":
            return self.addition()
        elif self.operand == "/":
            return self.division()
        elif self.operand == "*":
            return self.multiplication()
        elif self.operand == "%":
            return self.modulus()
        elif self.operand == "**":
            return self.exponentiation()
    
    def subtraction(self):
        """Subtracts number2  from number1"""
        return self.number1-self.number2

    def addition(self):
        """Adds values of number1 and number2"""
        return self.number1+self.number2

    def division(self):
        """Divides number1 by number2"""
        try:
            return self.number1/self.number2
        except ZeroDivisionError:
                return 'Infinity'
        
    def multiplication(self):
        """Multiplies values of number1 and number2"""
        return self.number1*self.number2

    def modulus(self):
        """Divides number1 by number2 and returns remainder"""
        return self.number1%self.number2

    def exponentiation(self):
        """Performs exponential calculation of number1 to the power number2"""
        return self.number1**self.number2
        
    
op_list = ["-","+","/","*","**","%"]

while True:
    calc = Calculator()
    calc.set_numbers()
    if not calc.check():
        break
    calc.first_float()
    if not calc.first_float():
        continue 
    calc.set_operand()
    if not calc.operand_check():
        continue
    calc.set_numbers()
    if not calc.check():
        break
    calc.second_float()
    if not calc.second_float():
        continue   
    print(calc.start())    

