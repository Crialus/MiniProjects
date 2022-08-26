import random

low_number = int(input(
    "What is the lowest number we shall play with: "))
high_number = int(input(
    "What is the highest number that we shall play with: "))


def we_guess(low_number, high_number):
    random_number = random.randint(low_number, high_number)
    guess = 0
    count = 0
    while guess != random_number:
        count += 1
        guess = int(input(
            f'Guess a random number between {low_number} and {high_number}: '))
        if guess < random_number:
            print(f'Sorry {guess} is too low')
            low_number = guess + 1
        elif guess > random_number:
            print(f'Sorry {guess} is too high')
            high_number = guess - 1
    print(f'Yay {guess} is correct, you win! It took you {count} tries')


def pc_guess(low_number, high_number):
    count = 0
    feedback = ''
    guess = int()
    while feedback != 'c':
        count += 1
        if low_number != high_number:
            guess = random.randint(low_number, high_number)
        else:
            guess = low_number

        feedback = input(
            f'I guess the number is {guess}:\n'
            'Is this too high (h) too low (l) or correct (c)?: \n')
        if feedback == 'h':
            high_number = guess - 1
        if feedback == 'l':
            low_number = guess + 1
    print(
        f'Yay, I guessed that your number was {guess} correctly, '
        f'it took me {count} tries')


print(f'Ok, the game will be played between {low_number} and {high_number}:')

game_type = input(
    "Would you like to guess a number (me) or have the computer guess (pc)?")

if game_type == 'me':
    we_guess(low_number, high_number)
elif game_type == 'pc':
    pc_guess(low_number, high_number)
