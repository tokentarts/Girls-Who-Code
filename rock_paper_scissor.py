#!/bin/python3
from random import randint

player = input('rock (r), paper (p), scissors (s) ?')
print(player, 'vs', end=' ')
computer = randint(1, 3)
# print(computer)

if computer == 1:
    rival = 'r'

elif computer == 2:
    rival = 'p'

else:
    rival = 's'

print(rival)

if player == rival:
    print('DRAW!')

elif player == 'r' and rival == 's':
    print('Player wins!')

elif player == 'r' and rival == 'p':
    print('Computer wins!')

elif player == 'p' and rival == 'r':
    print('Player wins!')

elif player == 'p' and rival == 's':
    print('Computer wins!')

elif player == 's' and rival == 'p':
    print('Player wins')

elif player == 's' and rival == 'r':
    print('Computer wins')
