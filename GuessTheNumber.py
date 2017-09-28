import random


def check(n, c):
    if n < c:
        return 1
    elif n > c:
        return 2
    elif n == c:
        return 3


def game():
    random_number = random.randrange(1, 100, 1)
    guess = 0

    while True:
        player_number = int(input('Pick your number:'))
        result = check(random_number, player_number)
        guess += 1

        if result == 3:
            print('Congratulations, You guessed the number! Guesses taken:', guess)
            break
        elif result == 2:
            print('The number is too small.')
        elif result == 1:
            print('The number is too big.')


game()
