from random import *
from sys import *
print('ROCK, PAPER, SCISSORS')
x=0
y=0
z=0
print(x,' Win,',y,'Loss',z,'Tie')
print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
m = input()
n=randint(1,3) #random number


#for random number choosing the guess
if n==1:
    compguess='ROCK'

elif n==2:
     compguess='PAPER'

else :
     compguess='SCISSORS'


#as from input
if m=='p':
    m='PAPER'

elif m=='r':
     m='ROCK'

elif m=='s':
    m='SCISSORS'


#main code
while True:

    print(m, 'versus...')
    print(compguess)
    if m == compguess: #if same
        print('It is a tie!')
        z=z+1
        print(x, ' Win,', y, 'Loss', z, 'Tie')
        exit()

    elif m=='ROCK' :
        if compguess=='PAPER':
            y=y+1
            print(x, ' Win,', y, 'Loss', z, 'Tie')
            exit()

        else:
            x=x+1
            print(x, ' Win,', y, 'Loss', z, 'Tie')
            exit()

    elif m=='PAPER' :
        if compguess=='ROCK':
            x=x+1
            print(x, ' Win,', y, 'Loss', z, 'Tie')
            exit()

        else:
            y=y+1
            print(x, ' Wins,', y, 'Losses', z, 'Ties')
            exit()

    elif m=='SCISSORS':
        if compguess=='ROCK':
            y=y+1
            print(x, ' Wins,', y, 'Losses', z, 'Ties')
            exit()

        else:
            x=x+1
            print(x, ' Wins,', y, 'Losses', z, 'Ties')
            exit()

    elif m=='exit':
         exit()
































