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
    guess = 1
    
    while True:
        player_number = int(input('Pick your number:'))
        result = check(random_number, player_number)

        if result == 3:
            print('Congratulations, You guessed the number! Guesses taken:', guess)
            break
        elif result == 2:
            guess += 1
            print('The number is bigger than you provided.')
        elif result == 1:
            guess += 1
            print('The number is smaller than you provided.')


game()
