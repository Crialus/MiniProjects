import random


class GuessingGame:
    def __init__(self, min, max, game_type):
        self.guesses = 0
        self.min = min
        self.max = max
        if game_type == 'me':
            self.user_play()
        else:
            self.computer_play()

    def user_play(self):
        self.number = random.randint(self.min, self.max)
        while True:
            self.guesses += 1
            if self.max == self.min:
                print(
                    f'The number is between {self.max} '
                    f'and {self.min}, let\'s assume you '
                    'were right this time. you used '
                    f'{self.guesses} attempts')
                return self.play_again()
            guess = self.get_guess()
            if guess < self.number:
                print(f'{guess} is too low, try again!')
                self.min = guess + 1
            elif guess > self.number:
                print(f'{guess} is too high, try again')
                self.max = guess - 1
            else:
                print(f'{guess} is correct, you used {self.guesses} attempts.')
                return self.play_again()

    def get_guess(self):
        guess = input(
            f'Guess a random number between {self.min} and {self.max}: ')

        if self.valid_number(guess):
            return int(guess)
        else:
            print(
                f'Please enter a valid number between {self.min} '
                f'and {self.max}: ')
            return self.get_guess()

    def valid_number(self, input):
        try:
            number = int(input)
        except Exception:
            return False
        return self.min <= number <= self.max

    def computer_play(self):
        self.feedback = ''
        while self.feedback != 'c':
            self.guesses += 1
            if self.min != self.max:
                self.guess = random.randint(self.min, self.max)
            else:
                self.guess = self.min
            feedback = self.get_feedback()
            if feedback == 'h':
                self.max = self.guess - 1
            elif feedback == 'l':
                self.min = self.guess + 1
            elif feedback == 'c':
                print(
                    f'Yay, I guessed that your number was {self.guess} '
                    f'it took me {self.guesses} attempts')
                return self.play_again()
            else:
                print(feedback)

    def get_feedback(self):
        self.feedback = input(
                f'I guess the number is {self.guess} '
                'is this too high(h), too low(l) '
                'or correct(c)? ').lower()
        if self.feedback in {'h', 'l', 'c'}:
            return self.feedback
        else:
            print('Please enter a valid response')
            return self.get_feedback()

    def play_again(self):
        choice = input('Would you like to play again Y/N: ').upper()
        if choice == 'Y':
            return game_init()
        else:
            return


def game_init():
    min = int(input('What is the lowest number to play with: '))
    max = int(input('What is the highest number to play with: '))
    choice = input(
            'Would you like to play a game where you guess a number that the '
            'computer thinks of (me) or a game where the computer guesses a '
            'number that you think of (pc): ').lower()
    if choice == 'me':
        pass
    elif choice == 'pc':
        pass
    else:
        print('Please enter a valid response')
        return game_init()
    GuessingGame(min, max, choice)


game_init()
