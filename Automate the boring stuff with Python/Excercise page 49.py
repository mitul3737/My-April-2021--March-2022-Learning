from random import *
from sys import *
print(' I m thinking of a number between 1 and 20')
print('Take a guess')
guess=int(input())
rguess=randint(1,20) #Getting the random number
count=1
while True:
    if rguess == guess:
        print('Good job! You guessed my number in ',count, 'guesses!')
        exit()
    elif rguess > guess:
        print('Your guess is too low')
        print('Take a guess')
        guess = int(input())
        count=count+1
    elif rguess < guess:
        print('Your guess is too high')
        print('Take a guess')
        guess = int(input())
        count=count+1

