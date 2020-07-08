import time
import random

class ticcy():
    def __init__(self, name):
        self.name = name

        self.board = []
        
        i = []

        for x in range(3):
            i.append("")

        for y in range(3):
            self.board.append(i)

        print(self.board)

    def havego(self, coord, typ):
        self.board[coord.x, coord.y] = typ

    def workout(self, typ):
        if (self.board == [['', '', ''], ['', '', ''], ['', '', '']]):
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            
            self.board[x, y] = typ
    
    def blank(self):
        i = []

        for x in range(3):
            i.append("")

        for y in range(3):
            self.board.append(i)

    def __str__(self):
        out = "[" + self.name + "]\n"
        
        for x in self.board:
            for y in x:
                out += y

            out += "\n"

        return out

class vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return str(x) + ", " + str(y)

a = ticcy("game1")