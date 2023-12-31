from itertools import permutations
import timeit, random
import src.Nqueens as nq
#* Generate all possible permutations of columns indices, with respect to the time limit.
    #* Check if the current permutation is a valid solution, If True:
        #* Add the permutation to the solutions list.
        
#! Very Slow After (n = 10).

def brute(board, time_limit_Sec= 9):
    
    start_time = timeit.default_timer()
    
    n = board.n
    solutions = []
    columns = range(n)


    if n < 4:
        return solutions # no solution under 4

    # loop through all possible solutions
    for permutation in permutations(columns):

        # if time limite reached break
        if timeit.default_timer() - start_time > time_limit_Sec:
            break

        # is solution is valid add it
        if n == len(set(permutation[i] + i for i in columns)) == len(set(permutation[i] - i for i in columns)):
            solutions.append(permutation)

    return solutions



def solve(solutions):
    n_solutions = len(solutions)
    d = len(str(n_solutions))

    for counter, solution in enumerate(solutions, start=1):
        print(f'[{counter :0{d}d}] -> {solution}')

    

def display(solutions,start_time,draws_num = 3):
    length = len(solutions)
    if length == 0:
        print("No solutions found")
    
    elif  draws_num > 11 and draws_num > length:
        print(f"Invalid Order, Choose a number between 1 and 10.")
    else:

        executed_time = timeit.default_timer() - start_time
        solve(solutions)
        print(f'\n{length} Solutions found within {round(executed_time, 5)} Seconds. Using Permutations Algorithm.')
    
        # display 3 random solutions
        # get the index of the 3
        draws_index = random.sample(range(length), draws_num)

        for index in draws_index:
            solution = solutions[index]
            d = len(str(length))

            print(f"\nSolution {index + 1:0{d}d}.")
            print(nq.Nqueens(1,solution))