#Conway's Game of Life

import random, time, copy
WIDTH=60
HEIGHT=20

#create a list of list for the cells:
nextCells=[]
for x in range(WIDTH):
    column=[]  #Create a new column
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#')  #Ad a living cell
        else:
             column.append(' ')  #Ad a dead cell
    nextCells.append(column)  #nextCells is a list of column lists

while True:  #Main program loop
    print('\n\n\n\n\n')
    currentCells=copy.deepcopy(nextCells)

#Print currentCells on the screen:
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(currentCells[x][y])  #print the # or space
    print()                        #Print a newline at the end of the row


#Calculate the next step's cell based on current steps's cell
for x in range(WIDTH):
    for y in range(HEIGHT):
        # Get neighbouring cordinates
        # '% WIDTH' ensures leftcoord is always between 0 and WIDTH -1
        leftCoord=(x-1)% WIDTH
        rightCoord=(x+1)%WIDTH
        aboveCoord=(y-1)%WIDTH
        belowCoord=(y+1)%WIDTH


        #Count number of living neighbours:
        numNeighbors=0
        if currentCells[leftCoord][aboveCoord]=='#':
            numNeighbors+=1       #top left neighbour is alive
        if currentCells[x][aboveCoord]=='#':
            numNeighbors+=1      #Top neighbor is alive
        if currentCells[rightCoord][aboveCoord]=='#':
            numNeighbors+=1      #Top right neighbor is alive
        if currenCells[leftCoord][y]:
            numNeighbors+=1      #Left neighbor is alive
        if currentCells[rightCoord][y]=='#':
            numNeighbors+=1     #Right neighbor is alive
        if currentCells[leftCoord][belowCoord]=='#':
            numNeighbors+=1     #Bottom left neighbor is alive
        if currenCells[x][belowCoord]=='#':
            numNeighbors+=1     #Bottom neighbor is alive
        if currentCells[rightCoord][belowCoord]=='#':
            numNeighbors+=1     #Bottom right neighbor is alive


        #Set cell based on Conway's Game of life rules:
        if currentCells[x][y]=='#' and (numNeighbors==2 or numNeighbors==3):
            #Living cells with 2 or 3 neighbors stay alive :
            nextCells[x][y]='#'
        elif currentCells[x][y]==' ' and numNeighbors==3:
            #Dead cells wiith 3 neighbors become alive:
            nextCells[x][y]='#'
        else:
            #Everything else dies or stay dead:
             nextCells[x][y]=' '

time.sleep(1)    #Add a 1-second pause to reduce flickering.







