import random

class GuessingGame:

    def __init__(self):
        self.computerNumber = random.randint(1, 9)
        self.counter = 0
        self.guess_number()

    def guess_number(self):
        self.guessNumber = input('\nType your number (1-9): ')
        if self.guessNumber == 'exit':
            self.game_over()
        else:
            self.guessNumber = int(self.guessNumber)
        self.compare()

    def set_counter(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

    def compare(self):
        self.set_counter()
        if self.computerNumber == self.guessNumber:
            print('\nCongratulations! You win!')
            print('\nNumber of tries: ', self.counter)
            game = GuessingGame()
        else:
            print('\nTry again!')
        self.guess_number()

    def game_over(self):
        exit()
        

game = GuessingGame()

