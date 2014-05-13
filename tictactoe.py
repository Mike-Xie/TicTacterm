# TTC wih AI started 5/8

import copy
import random
# represent a gameboard as an array with 9 elements

# print board


def printBoard(board):
    print board[0] + " | " + board[1] + " | " + board[2]
    print "-" * 10
    print board[3] + " | " + board[4] + " | " + board[5]
    print "-" * 10
    print board[6] + " | " + board[7] + " | " + board[8]
    print "\n"
# control flow
# alternate turns, put x and  into game
# can only move into non empty squares
# game ends if either player wins or game board is full
# otherwise people alternate turns

# helper functions
def validMove(board, square):
    return board[square] == ' '

def makeMove(board, square, letter):
        board[square] = letter
        #printBoard(board)

def isWinner(board, letter):
    won = [letter for i in range(3)]
    # diagonal
    # return value themselves rather than True, more readable
    return( (board[0::4] == won) or
    (board[2:7:2] == won) or
    # horizontal
    (board[:3]) == won or
    (board[3:6]) == won or 
    (board[6:]) == won or 
    # vertical
    (board[0:7:3]) == won or
    (board[1:8:3]) == won or
    (board[2::3]) == won)

def copyBoard(board):
    # for looking ahead for the AI
    return copy.deepcopy(board)

def isBoardFull(board):
    return board.count(' ') == 0
def isSquareEmpty(board, square):
    return board[square] == ' '

def AIHandler(board):
    AILetter = 'O'
    playerLetter = 'X'
    # look one move ahead 
    for i in range(9):
       copy = copyBoard(board)

       # this is inefficient, fix later
       if isSquareEmpty(copy, i):
            makeMove(copy, i, AILetter)
            if isWinner(copy, AILetter):
                return i
    # duplicate code, need to see if can condense somehow, but all attempts so far have failed
    for i in range(9):
       copy = copyBoard(board)
       if isSquareEmpty(copy, i):
            makeMove(copy, i, AILetter)
            if isWinner(copy, AILetter):
                return i
    # otherwise try to take corners, center, sides in decreasing priority
    # player 2 must take the center if a corner is taken
    corners = [0,2,6,8]
    center = [5]
    sides = [1,3,5,7]
    validC, validS = [], []
    for i in corners:
        if isSquareEmpty(board, i):
            validC.append(i)
    if len(validC) > 0:
        return random.choice(validC)
    if isSquareEmpty(board,5):
        return center[0]
    for i in sides:
        if validMove(board, i):
            validS.append(i)
    if len(validS) > 0:
        return random.choice(validC)
def humanHandler():
    print( "Where would you like to move? (Input:0 - 8 only)")
    move = input()
    return int(move)
def main():
    print( "Starting a game of Tic Tac Toe.")
    print( "This is how the indexes work.")
    show = [str(i) for i in range(9)]
    printBoard(show)
    board = [' ' for i in range(9)]  
    order = { 0: "You", 1: "AI"}
    turn = random.choice(range(2))
    print order[turn] + " gets first move!"
    print "\n"
    if turn == 0:
        printBoard(board)
    gameOver = False
    playerLetter = 'X'
    AILetter = 'O'
    while gameOver == False:
        if turn == 0: # human, prob bad design
            humanMove = humanHandler() 
            makeMove(board, humanMove, playerLetter)

            # check game over
            if isWinner(board, playerLetter):
                print "Player Wins" 
                printBoard(board)
                gameOver == True
                break
            else:
                if isBoardFull(board):
                    print "Cat's Game" 
                    printBoard(board)
                    gameOver == True
                    break
                else:
                    turn = 1
        else: # turn == 1 by default here
            AIMove = AIHandler(board) 
            print "AI Turn, chooses:" + str(AIMove)
            makeMove(board, AIMove, AILetter)
            
            printBoard(board)
            if isWinner(board, AILetter):
                print "AI Wins"
                printBoard(board)
                gameOver == True
                break    
            elif isBoardFull(board):
                print "Cat's Game"
                printBoard(board)
                gameOver == True
                break
            else:

                turn = 0
def test():
    board = [' ' for i in range(9)]
    makeMove(board, 2, 'X')
    makeMove(board, 4, 'X')
    makeMove(board, 6, 'X')
    makeMove(board, 8, 'X')
    makeMove(board, 1, 'X')
    print isWinner(board, 'X')
    print isWinner(board, 'O')
    print isBoardFull("bagels")
    print AIHandler(board)
    print AIHandler(board)

def test2():
    board = [' ' for i in range(9)] 
    makeMove(board, 0, 'X')
    makeMove(board, 4, 'x')
    printBoard(board)
    AIMove =  AIHandler(board)
    makeMove(board, AIMove, 'O')
    printBoard(board)
#print test2()

main()
