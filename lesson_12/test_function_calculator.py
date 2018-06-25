import unittest
from function_calculator import add, subtract, multiply, divide, calculation

class Calculator(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(add(5,4), 9)

    def testSubtract(self):
        self.assertEqual(subtract(5,4), 1)

    def testMultiply(self):
        self.assertEqual(multiply(5,4), 20)

    def testDivide(self):
        self.assertEqual(divide(5,4), 1.25)

    def testDivisionByZero(self):
        self.assertRaises(ZeroDivisionError, divide (0, 0))

    def testCalculation(self):
        self.assertEqual(calculation('5+4'), 9)
        

if __name__ == "__main__":
    unittest.main()
