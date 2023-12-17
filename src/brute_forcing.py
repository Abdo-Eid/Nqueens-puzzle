from random import randint
from copy import deepcopy
from itertools import permutations

# after n = 10 it is very slow


def brute(board):
    n = board.n
    sol = []
    col = range(n)
    for combo in permutations(col): #combo has all the possible positoin for queens
        # when there is only one queen in each diagonal
        if n == len(set(combo[i]+i for i in col)) == len(set(combo[i]-i for i in col)): # SOLUTION  
            sol.append(combo)
    return sol


def display(sol):
    g = 0
    for s in sol:
        g +=1
        print(*s)

    print(g)

