import random

SIGNS = ('rock', 'paper', 'scissors', 'lizard', 'spock')

player_1 = input('Enter your sign: ').lower()
player_2 = random.choice(SIGNS)

print('Player 1: ', player_1, 'Player 2: ', player_2)

while player_1 not in SIGNS:
    player_1 = input('Enter your sign: ').lower()

if player_1 == player_2:
    print('Tie!')
elif player_1 == 'rock':
    if player_2 in ('lizard', 'scissors'):
        print('Player 1 Won!')
    else:
        print('Player 2 Won!')
elif player_1 == 'paper':
    if player_2 in ('rock', 'spock'):
        print('Player 1 Won!')
    else:
        print('Player 2 Won!')
elif player_1 == 'scissors':
    if player_2 in ('paper', 'lizard'):
        print('Player 1 Won!')
    else:
        print('Player 2 Won!')
elif player_1 == 'lizard':
    if player_2 in ('spock', 'paper'):
        print('Player 1 Won!')
    else:
        print('Player 2 Won!')
elif player_1 == 'spock':
    if player_2 in ('scissors', 'rock'):
        print('Player 1 Won!')
    else:
        print('Player 2 Won!')
