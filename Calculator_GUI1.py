from tkinter import *

class CalcGUI:
    def __init__(self, master):
        self.master = master
        master.title('Calculator')
        self.lbl = Label(master, width = 30, height = 2 ,bg = 'white', relief = 'groove')
        self.lbl.grid(row = 0, column = 0,columnspan = 5, pady = (10,5), padx = 20)
       
        self.btn1 = Button(master, text='1', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("1"))
        self.btn1.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.btn2 = Button(master, text='2', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("2"))
        self.btn2.grid(row = 1, column = 1, pady = 5, padx = 5)
        self.btn3 = Button(master, text='3', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("3"))
        self.btn3.grid(row = 1, column = 2, pady = 5, padx = 5)
        self.btnbs = Button(master, text='<--', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = self.bs)
        self.btnbs.grid(row = 1, column = 3, pady = 5, padx = 5)
        self.btnad = Button(master, text='+', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("+"))
        self.btnad.grid(row = 1, column = 4, padx = 5, pady = 5)
        self.btn4 = Button(master, text='4', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("4"))
        self.btn4.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.btn5 = Button(master, text='5', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("5"))
        self.btn5.grid(row = 2, column = 1, pady = 5)
        self.btn6 = Button(master, text='6', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("6"))
        self.btn6.grid(row = 2, column = 2, pady = 5)
        self.btncl = Button(master, text='Clear', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = self.cl)
        self.btncl.grid(row = 2, column = 3, padx = 5, pady = 5)
        self.btnsub = Button(master, text='-', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("-"))
        self.btnsub.grid(row = 2, column = 4, padx = 5, pady = 5)
        self.btn7 = Button(master, text='7', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("7"))
        self.btn7.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.btn8 = Button(master, text='8', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("8"))
        self.btn8.grid(row = 3, column = 1, pady = 5)
        self.btn9 = Button(master, text='9', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("9"))
        self.btn9.grid(row = 3, column = 2, pady = 5)
        self.btneq = Button(master, text='=', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9')
        self.btneq.grid(row = 3, column = 3, padx = 5, pady = 5)
        self.btndiv = Button(master, text='/', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("/"))
        self.btndiv.grid(row = 3, column = 4, padx = 5, pady = 5)
        self.btn0 = Button(master, text='0', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("0"))
        self.btn0.grid(row = 4, column = 1, pady = 5)
        self.btnmult = Button(master, text='*', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("*"))
        self.btnmult.grid(row = 4, column = 3, padx = 5, pady = 5)
        self.btnmod = Button(master, text='%', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("%"))
        self.btnmod.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.btnexp = Button(master, text='**', width = 5, height = 2, relief = 'groove', bg = '#F9F9F9', command = lambda: self.btnevent("**"))
        self.btnexp.grid(row = 4, column = 2, padx = 5, pady = 5)
    op_list = ["-","+","/","*","**","%"]
    def btnevent(self,btn):
        if btn in self.op_list:
            if len(self.lbl['text'])!= 0:
                for i in self.op_list:
                    if i in self.lbl['text']:
                        break
                    else:
                        return True
                        
        else:
            self.lbl['text'] += btn
        
    def bs(self):
        self.lbl['text'] = self.lbl['text'][:-1]
    def cl(self):
        self.lbl['text'] = ''
        
mainWindow = Tk()
mainWindow.geometry('275x260')
my_calc = CalcGUI(mainWindow)
mainWindow.mainloop()

