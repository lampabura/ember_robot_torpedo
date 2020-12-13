from helpers import State
from random import randrange
import numpy as np

class Game:
    state = State.START
    board_size = 5
    boat_size = 2
    max_boat_number = 3
    
    def __init__(self):
        self.board = [[" " for i in range(self.board_size)] for j in range(self.board_size)]
        self.target_board = [[" " for i in range(self.board_size)] for j in range(self.board_size)]

    def start(self):
        self.state = State.INGAME
        self.placeBoats()
        self.printBoard()

    def placeBoats(self):
        for i in range(self.max_boat_number):
            self._placeBoat(i)
        self.boat_alive = self.max_boat_number

    def _placeBoat(self,id):
        while True:
            x = randrange(0, self.board_size)
            y = randrange(0, self.board_size)
            if self.board[x][y] != ' ': continue

            if x+1 < self.board_size and self.board[x+1][y] == ' ':  self.board[x+1][y] = id
            elif x-1 > 0 and self.board[x-1][y] == ' ':  self.board[x-1][y] = id
            elif y+1 < self.board_size and self.board[x][y+1] != ' ':  self.board[x][y+1] = id
            elif y-1 > 0 and self.board[x][y-1] == ' ':  self.board[x][y-1] = id
            else: continue

            self.board[x][y] = id
            break
        
    def stepEnemy(self, row, column):
        print("ENEMY: ", row, "-", column)
        character = self.board[row][column]
        self.board[row][column] = 'X'
        self.printBoard()

        if character != " ": return True  # return true if got hit our ship
        else: return False
    
    def getStep(self):
        while True:
           x = randrange(0, self.board_size)
           y = randrange(0, self.board_size)
           if self.target_board[x][y] == 'O': continue
           self.target_board[x][y] = 'O'
           return x , y

    def _countBoats(self):
        count = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] != 'X' and self.board[i][j] != ' ' : count += 1
        return count

    def isEnded(self):
        if self._countBoats() <= 0 and self.state >= State.INGAME: return True
        else: return False

    def printBoard(self):
        print(np.matrix(self.target_board))
        print("=================")
        print(np.matrix(self.board))
    
    def ended(self):
        self.state = State.END
