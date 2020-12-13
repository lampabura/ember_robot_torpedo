import random


board = [[0]*5]*5

def print_board(board):
    for row in board:
        for col in row:
            print(col,end="")
        print()

print(board)
print_board(board)



shipA_row = random.randint(0,5)
shipA_col = random.randint(0,5)
shipB_row = random.randint(0,5)
shipB_col = random.randint(0,5)



guess_row = random.randint(0,5)
guess_col = random.randint(0,5)

def turn(guess_row, guess_col):
    if(guess_row == shipA_row and guess_col == shipA_col):
        print("hit")
    else:
        if(guess_row < 0 or guess_row > 5 or guess_col < 0 or guess_col > 5):
            print("ha?!?!?!?")
        else:
            print("nope")
