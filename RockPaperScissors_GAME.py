""" ROCK, PAPER & SCISSOR GAME"""

import random
import time
player_name = input('Provide, Player Name: ')

print(f'Welcome {player_name.upper()} to the ROCK, PAPER & SCISSORS GAME'.center(100))
print('YOU ARE PLAYING AGAINST COMPUTER\n')
print('GAME is going to start in few min.\n')
time.sleep(5)
print('*'*50)

while True:
    player = input(f'\n{player_name.upper()}: Rock, Paper, Scissors or exit? ')
    computer = random.choice(['Rock', 'Paper', 'Scissors'])

    if player == computer:
        print('Tie!')

    elif player == 'Rock':
        if computer == 'Paper':
            print('You Lose!', computer, 'covers', player)
        else:
            print('You Win!', player, 'smashes', computer)

    elif player == 'Paper':
        if computer == 'Scissors':
            print('You Lose!', computer, 'cut', player)
        else:
            print('You Win!', player, 'covers', computer)

    elif player == 'Scissors':
        if computer == 'Rock':
            print('You Lose...', computer, 'Smashes', player)
        else:
            print('You Win!', player, 'cut', computer)

    else:
        exit()
