import time
import msvcrt
import os
from Board import *

def __init__():
    global KeyStroke
    global Game
    KeyStroke = ""
    Game = True

    global CounterY
    global CounterX
    CounterY = 0
    CounterX = (Board_Length - 1) // 2

    global Counter
    global CurrentPlayer
    Counter = "X"
    CurrentPlayer = 1

    UpdateBoard(CounterY, CounterX, Counter)
    GetPrintBoard()

def ChangePlayer():
    global CurrentPlayer
    global Counter
    global CounterY
    global CounterX

    if CurrentPlayer == 1:
        CurrentPlayer = 2
        Counter = "O"
        
    elif CurrentPlayer == 2:
        CurrentPlayer = 1
        Counter = "X"

    CounterY = 0
    CounterX = (Board_Length - 1) // 2

    UpdateBoard(CounterY, CounterX, Counter)
    GetPrintBoard()

def MoveRight():
    global CounterX
    if CounterX + 1 == Board_Length - 1:
        pass
    else:
        CounterX += 1
        UpdateBoard(CounterY, CounterX, Counter)
        UpdateBoard(CounterY, CounterX - 1, "-")
        GetPrintBoard()

def MoveLeft():
    global CounterX
    if CounterX - 1 == 0:
        pass
    else:
        CounterX -= 1
        UpdateBoard(CounterY, CounterX, Counter)
        UpdateBoard(CounterY, CounterX + 1, "-")
        GetPrintBoard()

def PlaceCounter():
    global Board
    global CounterX
    global CounterY
    global Counter

    for i in range(Board_Height):
        if Board[i][CounterX] == " ":
            if Board[i + 1][CounterX] != " ":
                FreeSpace = i

                UpdateBoard(CounterY, CounterX, "-")
                UpdateBoard(FreeSpace, CounterX, Counter)
                GetPrintBoard()
                ChangePlayer()
                break
            
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
        elif KeyStroke == b"d":
            MoveRight()
            KeyStroke = ""
        elif KeyStroke == b" ":
            PlaceCounter()
            KeyStroke = ""

if __name__ == "__main__":
    Main()

time.sleep(1000)
