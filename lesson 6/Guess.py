import random

class Guess:

    def __init__(self):
        self.computerNumber = random.randint(1, 9)

    def guess_number(self, number):
        self.guessNumber = number

    def compare(self):
        self.counter += 1
        if self.computerNumber == self.guessNumber:
            print('\nCongratulations! You win!')
            print('\nNumber of tries: ', self.counter)
            game = Guess()
            self.counter = 0
        else:
            print('\nTry again!')

game = Guess()

game.counter = 0

while True:

    input_string = int(input('\nType your number: ')) 

    if input_string == 'exit':

        break

        game.counter = 0

        del game

    else:

        game.guess_number(input_string)

        game.compare()
