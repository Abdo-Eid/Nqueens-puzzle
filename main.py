from src.Nqueens import Nqueens
import src.hill_climbing as climbing
import src.hill_climbingS as climbingS
import src.brute as brute
import src.genatic as gen
import timeit

# initial board
# only n for random
# n, initial positioin if wanted
n = 8
board = Nqueens(n)


# #! ---------- Brute Forcing ---------------------------------------------------------------------------------------------------- !#
# time_limit = 3
# start_time = timeit.default_timer()

# #? -------------------- Using Permutations -------------------- ?#   Very Slow After (n = 10).

# solutions = brute.force(board, time_limit)
# brute.display(solutions,start_time)


# # ? -------------------- Using Backtracking -------------------- ?#   Slower After (n = 14).

# solutions = brute.backtracking(board, time_limit)

# brute.display(solutions,start_time)

# # ? ------------------------------------------------------------ ?#

# stop_time  = timeit.default_timer()
# executed_time = stop_time - start_time



#! ---------- Hill Climbing ---------------------------------------------------------------------------------------------------- !#

# # ? -------------------- Speady -------------------- ?#

# start_1 = timeit.default_timer()

# solution = climbingS.hill_climbing(board)
# print(solution.pos)
# print(solution) 
# print(solution.conflicts())

# stop_1 = timeit.default_timer()

# time_1 = stop_1 - start_1
# print('Fast approach Time: ', round(time_1, 10), 'Seconds.')

# #? -------------------- Normal -------------------- ?#

# start_2 = timeit.default_timer()

# solution = climbing.hill_climbing(board)
# print(solution.pos)
# print(solution)
# print(solution.conflicts())

# stop_2 = timeit.default_timer()
# time_2 = stop_2 - start_2

# print('Normal approach Time: ', round(time_2, 10), 'Seconds.') 

# #? ------------------------------------------------ ?#

# print('First is', round(time_2/time_1, 5), 'x faster')

# #? ------------------------------------------------ ?#


# #! ------------ Genatic ---------------------------------------------------------------------------------------------- !#

start = timeit.default_timer()

solution = gen.genatic(n)
print(solution.pos)
print(solution)
print(solution.conflicts())

stop = timeit.default_timer()
time_2 = stop - start

print('Time: ', round(time_2, 10), 'Seconds.') 
