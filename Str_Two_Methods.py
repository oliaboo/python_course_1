class Printer():
    def set_string(self,your_str):
        self.your_str = your_str

    def print_string(self):
        try:
            print(self.your_str)
        except AttributeError:
            print('no name')

I_am_string = Printer()
I_am_string.set_string('stirngstringstring')
I_am_string.print_string()
        
