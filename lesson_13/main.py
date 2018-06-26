import csv
from calculator.calculator import Calculator
from tkinter import *
import re

class MyGUI:

    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Calculator")
        self.label_1 = Label(self.main_window, text = 'Write an expression ex.: A*B', width=20)
        self.label_1.pack()
        self.entry_1 = Entry(self.main_window, width = 24)
        self.entry_1.pack()
        self.but_2 = Button(self.main_window, text = 'AC', width=20, command = self.AC)
        self.but_2.pack()
        self.but_3 = Button(self.main_window, text = 'Calculate', width=20, command = self.calculate)
        self.but_3.pack()
        self.but_4 = Button(self.main_window, text = 'History', width=20, command = self.history)
        self.but_4.pack()
        self.txt_1 = Text(self.main_window, height=10, width=25)
        self.txt_1.pack()

    def AC(self):
        self.entry_1.delete(0, END)

    def history(self):
        global counter
        counter += 1
        if counter % 2 == 0:
            self.txt_1.delete(1.0, END)
        else:
            self.txt_1.delete(1.0, END)
            with open('history.csv', 'r') as f:
                reader = csv.reader(f, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    if row != []:
                        string = "{0} {1} {2} = {3}\n".format(row[0], row[2], row[1], row[3]) 
                        self.txt_1.insert(END, string)

    def calculate(self):
        raw_expression = self.entry_1.get()
        pattern = r'^(\d+(\.\d+)?)\s*([\+\-\/\*])\s*(\d+(\.\d+)?)$'
        matcher = re.match(pattern, raw_expression)
        if matcher:
            x = float(matcher.group(1))
            y = float(matcher.group(4))
            operation = matcher.group(3)
            result = Calculator.calculation(x, y, operation)
            self.entry_1.delete(0, END)
            self.entry_1.insert(END, result)
        else:
            self.entry_1.delete(0, END)
            self.entry_1.insert(END, "Expression Error!")

with open('history.csv', 'w') as f:
	f.close()
counter = 0
main_window = Tk()
gui = MyGUI(main_window)
main_window.mainloop()
