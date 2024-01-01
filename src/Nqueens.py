import random
from copy import deepcopy

class Nqueens:
    def __init__(self, n,pos = []) -> None:
        # if pos is given ignore n
        # position list is one dim sice we considered only one queen per raw
        # pos list has the index is the rows and elements is the columns
        if pos == []:
            self.pos = [random.randint(0,n-1) for _ in range(n)]
            self.n = n
        else:
            self.pos = pos
            self.n = len(pos)


        self.empty_board = [['- ']*self.n for _ in range(self.n)] # empty board
        self.board = self.putInPos(self.empty_board,self.pos) 
        self.queens_pos = self.queens_p()


    # display the board
    def __str__(self):
        d = len(str(self.n))
        t = ""
        b = ["".join(row) for row in self.board]
        for i,e in enumerate(b):
            t += f'{i:0{d}d}. {e}\n'
        return t
    
    # put queens with positon 'pos' on the board
    @staticmethod
    def putInPos(board,pos):
        b = deepcopy(board)
        for row,col in enumerate(pos):
            b[row][col] = 'Q '
        return b
    
    # return how many queens in each column,postive and negative diagonals
    def queens_p(self):
        col_queens = [0] * self.n
        posdiag_queens = [0] * (2 * self.n - 1)
        negdiag_queens = [0] * (2 * self.n - 1)
        for row,col in enumerate(self.pos):
            col_queens[col] +=1
            posdiag_queens[col - row + self.n - 1] +=1
            negdiag_queens[col + row] +=1

        return [col_queens,posdiag_queens,negdiag_queens]

    # change position of queen on the board
    def changePos(self,old_row,col):
        self.board[old_row][self.pos[old_row]],self.board[old_row][col] = self.board[old_row][col],self.board[old_row][self.pos[old_row]]

        #change conflicts when change place
        self.queens_pos[0][self.pos[old_row]] -=1
        self.queens_pos[1][self.pos[old_row] - old_row + self.n - 1] -=1
        self.queens_pos[2][self.pos[old_row] + old_row] -=1

        self.pos[old_row] = col

        self.queens_pos[0][col] +=1
        self.queens_pos[1][col - old_row + self.n - 1] +=1
        self.queens_pos[2][col + old_row] +=1

    # calc the conflict for spicific row or queen
    def confilct(self,queen_row):
        return (self.queens_pos[0][self.pos[queen_row]] + self.queens_pos[1][self.pos[queen_row] - queen_row + self.n-1] + self.queens_pos[2][self.pos[queen_row] + queen_row]) - 3

    def conflicts(self) -> int:
        c = deepcopy(self.queens_pos)
        con = 0
        for queen_row in range(self.n):
            con += (c[0][self.pos[queen_row]] + c[1][self.pos[queen_row] - queen_row + self.n-1] + c[2][self.pos[queen_row] + queen_row]) - 3
            c[0][self.pos[queen_row]] -=1
            c[1][self.pos[queen_row] - queen_row + self.n-1] -=1
            c[2][self.pos[queen_row] + queen_row] -=1

        return con
    
    def copy(self):
        return deepcopy(self)
    
    def has_conflict(self):
        for r in range(self.n):
            if self.confilct(r) > 0:
                return True
        return False
    
    def re_queen_pos(self):
        self.queens_pos = self.queens_p()

    # @staticmethod
    # def empty(n):
    #     self = Nqueens(n)
    #     self.board = self.empty_board
    #     return self