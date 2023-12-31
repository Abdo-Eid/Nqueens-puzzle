from src.Nqueens import Nqueens
import src.hill_climbing as climbing
import src.hill_climbingS as climbingS
import src.brute_forcing as force
import src.back_tracking as back
import timeit

# initial board
# only n for random
# n, initial positioin if wanted
board = Nqueens(5)


## example of hillclimbing

"""
start = timeit.default_timer()

solution = climbingS.hill_climbing(board)
print(solution.pos) # get positions
print(solution) 
print(solution.conflicts()) # number of conflicts or attacks

stop = timeit.default_timer()
t1 = stop - start
print('Fast approach Time: ', t1)

print 

start = timeit.default_timer()

solution = climbing.hill_climbing(board)
print(solution.pos)
print(solution)
print(solution.conflicts())

stop = timeit.default_timer()
t2 = stop - start
print('Normal approach Time: ', t2) 

print('first is',t2/t1,'x faster')

"""

# brute forcing using permutation

"""
start = timeit.default_timer()

solutions = force.brute(board)
force.display(solutions)

stop = timeit.default_timer()

print('Time: ', stop - start) 

"""

# brute forcing using back tracking


start = timeit.default_timer()

solutions = back.brute(board)
back.display(solutions)

stop = timeit.default_timer()

print('Time: ', stop - start) 
