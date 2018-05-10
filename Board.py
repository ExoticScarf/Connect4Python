import os
import random
import time

global PrintBoard
global Board

Board = []
Board_Height = 6 
Board_Length = 10
## Should be an odd number
PrintBoard = ""

## Lower ==> Higher
##   ||
##   ||
##   \/
## Higher

def MakeBoard(): ## Do not use more than once
    
    for y in range(Board_Height) : ## Creates dictionary ## List of lists
        Board.append([])           ## Will be y coord

        for x in range(Board_Length) : ## x coord

            if x == 0 and y == 0 :           ## checks for position and
                Board[y].append("+")         ## sets value for board
            elif x == Board_Length - 1 and y == 0 :
                Board[y].append("+")
            elif x == 0 and y == Board_Height - 1 :
                Board[y].append("+")
            elif x == Board_Length - 1 and y == Board_Height - 1 :
                Board[y].append("+")

            elif x == 0 :
                Board[y].append("|")
            elif x == Board_Length - 1 :
                Board[y].append("|")

            elif y == 0 :
                Board[y].append("-")
            elif y == Board_Height - 1 :
                Board[y].append("-")
            
            else:
                Board[y].append(" ")

def UpdateBoard(Update_y, Update_x, Update): ## Updates board with new value
    if Update_y != Board_Height - 1:
        if Update_x != 0 and Update_x != Board_Length - 1:
            Board[Update_y][Update_x] = Update

    

##  Turns Board into a multiline string
def GetPrintBoard():
    global PrintBoard
    PrintBoard = """"""

    for y in range(Board_Height):
        for x in range(Board_Length):
            PrintBoard += Board[y][x]

        if y < Board_Height - 1:
            PrintBoard += "\n"


    os.system("cls")
    print(PrintBoard)