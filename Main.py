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

def PlaceCounter():
    global CounterX, CounterY, Board, GhostX, GhostY
    UpdateBoard(CounterY, CounterX, "-")
    ChangePlayer()

    GhostX = (Board_Length - 1) // 2
    for i in range(Board_Height):
        if Board[i][CounterX] == " ":
            if Board[i + 1][CounterX] != " ":
                GhostY = i

    GenerateGhost()
            
def Main():
    global KeyStroke
    MakeBoard()
    __init__()

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
        

if __name__ == "__main__":
    Main()

time.sleep(1000)
