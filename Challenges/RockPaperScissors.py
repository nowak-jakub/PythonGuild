import random

SIGNS = ('rock', 'paper', 'scissors', 'lizard', 'spock')

player_1 = input('Enter your sign: ').lower()
player_2 = random.choice(SIGNS)

while player_1 not in SIGNS:
    player_1 = input('Enter your sign: ').lower()

print('Player 1: ', player_1, 'Player 2: ', player_2)

if player_1 == 'rock' and player_2 == 'paper':
    print('Player 2 Won!')
elif player_1 == 'scissors' and player_2 == 'paper':
    print('Player 1 Won!')
elif player_1 == 'scissors' and player_2 == 'rock':
    print('Player 2 Won!')
elif player_1 == 'paper' and player_2 == 'rock':
    print('Player 1 Won!')
elif player_1 == 'paper' and player_2 == 'scissors':
    print('Player 2 Won!')
elif player_1 == 'rock' and player_2 == 'scissors':
    print('Player 1 Won!')
elif player_1 == 'rock' and player_2 == 'lizard':
    print('Player 1 Won!')
elif player_1 == 'lizard' and player_2 == 'rock':
    print('Player 2 Won!')
elif player_1 == 'spock' and player_2 == 'lizard':
    print('Player 2 Won!')
elif player_1 == 'lizard' and player_2 == 'spock':
    print('Player 1 Won!')
elif player_1 == 'rock' and player_2 == 'lizard':
    print('Player 1 Won!')
elif player_1 == 'lizard' and player_2 == 'rock':
    print('Player 2 Won!')
elif player_1 == 'spock' and player_2 == 'scissors':
    print('Player 1 Won!')
elif player_1 == 'scissors' and player_2 == 'spock':
    print('Player 2 Won!')
elif player_1 == 'scissors' and player_2 == 'lizard':
    print('Player 1 Won!')
elif player_1 == 'lizard' and player_2 == 'scissors':
    print('Player 2 Won!')
elif player_1 == 'rock' and player_2 == 'spock':
    print('Player 2 Won!')
elif player_1 == 'spock' and player_2 == 'rock':
    print('Player 1 Won!')
elif player_1 == 'spock' and player_2 == 'paper':
    print('Player 2 Won!')
elif player_1 == 'paper' and player_2 == 'spock':
    print('Player 1 Won!')
elif player_1 == 'paper' and player_2 == 'lizard':
    print('Player 2 Won!')
elif player_1 == 'lizard' and player_2 == 'paper':
    print('Player 1 Won!')
elif player_1 == player_2:
    print('Tie!')