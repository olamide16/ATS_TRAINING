import re
from typing import Tuple


board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
currentPlayer = "X"
winner = None
gameRunning = True
def printBoard(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])
        print("---------")
# printBoard(board)
def playerInput(board):
    inp = input("Enter a number 1-9: ")
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Opps player is already in that spot!")
        
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner =  board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkslant(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]        
        
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkwin():
    if checkHorizontal(board) or checkRow(board) or checkslant(board):
        print(f"The winner is {winner}")

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkTie(board)
    checkwin()
    switchPlayer()