# Sudoku Solver by Mike Xie
# Input a string of 81 characters from 1-9 & . to represent empty
# because python list comprehensions make life easier
# Output a string of 81 characters only from 1-9 (solved)
# a Sudoku board is 9 x 9 grid, the goal is to fill each column, row and 3x3 sub-grid
# with the numbers 1 - 9, the puzzle setter providing a partially completed grid
# which should have one unique solution, individual members of board are squares
# Sudoku means 'single number' and was originally named 'Number Place'
# each square is a member of a column, row and sub-grid
# step 0: don't panic, step 1: think of I/O, step 2: outline how, step 3: fill in the code at the last and test

# I will use [A - I] for columns and [1-9] for rows, algebraic notation from chess days
# A1 top left corner, I9 bottom right corner
# Set up the board tiles much in the same way as creating a deck of cards

colIndex = "ABCDEFGHI"
rowIndex = "123456789"

def squaremaker(xList, yList):
    # returns an array of every combination of elements from 2 input lists
    return [i+j for i in xList for j in yList]

# all 81 squares in one list: A1, A2 . . I9, done by feeding in all of the indexes
squares = squaremaker(colIndex, rowIndex)

# data structures are the most important part, some guy who knew what he was talking about said
# if you give me the correct data structures I can figure out the algorithms
# A1 belongs in row A, column 1 and sub-grid A1, A2, A3, B1, B2, B3, C1, C2, C3
# a human player keeps this stuff in mind and knows that there can only be 1 instance
# of 1-9 in each of these regions and keeps a tally in their head
# they start by looking at squares that can only have 1 answer and then they put it in
# we can have each square be a key in a dictionary with values 1-9 and cross them off as they are no longer possible 
# update the rest of dictionaries, whenever we put a number in because somewhere some values are no longer valid and keep doing this until the puzzle is 
# I'm glad I started working on that Scheme parser earlier 

def gridParse(gridList):
    # returns a dictionary with keys as squares and starting grid entries as entries.
    # ex: {A1: 4, A2: 6, A3: .}
    # thank you stack overflow map 2 lists into dictionary
    dictionary = dict(zip(squares, gridList))
    assert len(dictionary) == 81
    return dictionary

        
def gridPosVal(parsedGrid):
    # returns a dictionary with keys as squares and all possible values as entries
    pass
# done, or at least that's how it works for easy/medium ones, never really got that much
# into it, was playing chess instead
# probably helps if we give that tally thing combination of col, row and subgrid a name
# let's use group, as in control group (from RTS games) and call the 21 members units (from RTS) 
# A1 is a unit in 3 groups, row, col, sub-grid
# there are 27 units then, 9 rows, 9 cols, 9 sub-grids
# I feel like I have duplicate code everywhere, w.e fix it later

# we want 9 lists of length 9 so use square maker which returns lists but feed in only one
# of the y co ordinate at a time but do it 9 times
def colMaker(xList, yList):
    # returns len(yList) of lists of elements in xList
    return [squaremaker(xList, number) for number in yList]

colList = colMaker(colIndex, rowIndex)
# same deal for the rows, we just do it the other way around
# wait, we can just call colMaker but feed xList and yList backwards
rowList = colMaker(rowIndex, colIndex)

# sub-grids, how to make sub-grids
# well it looks like colMaker('ABC','123') + . . . colMaker('GHI','789') 
subGridList =[ colMaker(row, col) for row in ('ABC','DEF','GHI') for col in ('123','456','789')]
# we want to probably store every square's units in a dictionary for some
# some reason but we will have to use set() on it first because we have
# duplicates
# don't optimize this right now! bad habit! bad habit!









# these test out the way we're expecting them to, awesome.

def test():
    easy = """
            .931.564.
            7.......5
            5.12.93.7
            2.......3
            .369.752.
            9.......1
            3.24.81.9
            6.......4
            .473.285.
"""
    assert len(colList) == 9
    assert len(subGridList) == 9 
    #print squares
    print "test"
    #print colList
    #print rowList
    #print subgridList
    print gridParse(easy)
   # print gridParse(subGridList)
test()
