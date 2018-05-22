import time
import msvcrt
import os
from Board import *

def __init__():
    global KeyStroke, Game
    KeyStroke = ""
    Game = True

    global CounterY, CounterX
    CounterY = 0
    CounterX = (Board_Length - 1) // 2

    global GhostX, GhostY
    GhostX = CounterX
    GhostY = Board_Height - 1

    global Counter, CurrentPlayer
    Counter = "X"
    CurrentPlayer = 1

    MakeBoard()
    UpdateBoard(CounterY, CounterX, Counter)
    GenerateGhost()
    GetPrintBoard()

def ChangePlayer():
    global CurrentPlayer, CounterX, CounterY, Counter
    if CurrentPlayer == 1:
        CurrentPlayer = 2
        Counter = "O"
        
    elif CurrentPlayer == 2:
        CurrentPlayer = 1
        Counter = "X"

    CounterY = 0
    CounterX = (Board_Length - 1) // 2    

    UpdateBoard(CounterY, CounterX, Counter)
    
def MoveRight():
    global CounterX
    if CounterX + 1 == Board_Length - 1:
        pass
    else:
        CounterX += 1
        UpdateBoard(CounterY, CounterX, Counter)
        UpdateBoard(CounterY, CounterX - 1, "-")
        GenerateGhost()

def MoveLeft():
    global CounterX
    if CounterX - 1 == 0:
        pass
    else:
        CounterX -= 1
        UpdateBoard(CounterY, CounterX, Counter)
        UpdateBoard(CounterY, CounterX + 1, "-")
        GenerateGhost()

def GenerateGhost():
    global GhostY, GhostX
    UpdateBoard(GhostY, GhostX, " ")
    
    for i in range(Board_Height):
        if Board[i][CounterX] == " ":
            if Board[i + 1][CounterX] != " ":
                GhostY = i
                GhostX = CounterX

                UpdateBoard(GhostY, GhostX, Counter)
                break

def CheckWinState():  ##  MAKE MORE EFFICIENT LATER
    global GhostX, GhostY, Counter, Board, Game
    Win = 0

    for i in range(1):
        for x in range(4):
            if Board[GhostY][GhostX + x] != Counter:
                Win = 0
                break
            else:
                Win += 1

        if Win == 4:
            Win = True
            break

        for x in range(4):
            if Board[GhostY][GhostX - x] != Counter:
                Win = 0
                break
            else:
                Win += 1

        if Win == 4:
            Win = True
            break

        for x in range(4):
            if Board[GhostY + x][GhostX] != Counter:
                Win = 0
                break
            else:
                Win += 1

        if Win == 4:
            Win = True
            break

        for x in range(4):
            if Board[GhostY - x][GhostX] != Counter:
                Win = 0
                break
            else:
                Win += 1

        if Win == 4:
            Win = True
            break

        for x in range(4):
            if Board[GhostY + x][GhostX + x] != Counter:
                Win = 0
                break
            else:
                Win += 1

        if Win == 4:
            Win = True
            break

        for x in range(4):
            if Board[GhostY + x][GhostX - x] != Counter:
                Win = 0
                break
            else:
                Win += 1

        if Win == 4:
            Win = True
            break

        for x in range(4):
            if Board[GhostY - x][GhostX - x] != Counter:
                Win = 0
                break
            else:
                Win += 1

        if Win == 4:
            Win = True
            break

        for x in range(4):
            if Board[GhostY - x][GhostX + x] != Counter:
                Win = 0
                break
            else:
                Win += 1

        if Win == 4:
            Win = True
            break
                
    if Win:
        Game = False
        ## End
                
def PlaceCounter():
    global CounterX, CounterY, Board, GhostX, GhostY
    UpdateBoard(CounterY, CounterX, "-")
    CheckWinState()
    ChangePlayer()

    GhostX = (Board_Length - 1) // 2
    for i in range(Board_Height):
        if Board[i][CounterX] == " ":
            if Board[i + 1][CounterX] != " ":
                GhostY = i

    GenerateGhost()
            
def Main():
    global KeyStroke, Board
    
    __init__()
    print(Board)
    input()
    
    while Game:

        if msvcrt.kbhit():
            KeyStroke = msvcrt.getch()

        if KeyStroke == b"a":
            MoveLeft()
            KeyStroke = ""
            GetPrintBoard()
            
        elif KeyStroke == b"d":
            MoveRight()
            KeyStroke = ""
            GetPrintBoard()
            
        elif KeyStroke == b" ":
            PlaceCounter()
            KeyStroke = ""
            GetPrintBoard()

def GameStart():
    global CurrentPlayer, Board
    Main()

    if CurrentPlayer == 1:
        CurrentPlayer = 2
    else:
        CurrentPlayer = 1

    print("Game Over, Player", CurrentPlayer, "loses")

    print("\nDo you wish to play again?")
    Again = input().lower()
    if Again.startswith("y"):
        #Board = []
        GameStart()

if __name__ == "__main__":
    GameStart()
