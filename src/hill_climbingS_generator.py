from random import randint
from src.Nqueens import Nqueens

# it does one iteration per second almost
def hill_climbing(board_sie, max_iterations=50050,non_improving_limit = 10040):
    # Start with a random initial state
    n = board_sie
    current_state = Nqueens(n)
    current_conflicts = current_state.conflicts()

    non_improving_counter = 0
    for iteration in range(max_iterations):
        # If the current state is a solution, return it
        if current_conflicts == 0:
            yield (current_state,'soluton found')
            return
        
        yield (current_state,f'iteration {iteration} conflict {current_conflicts}')

        # another approtch is to get random queen change the pos to random col
        # if there improve select that state
        for _ in range(n^2):
            queen = randint(0,n-1) # index of the row
            col = randint(0,n-1) 
            # if the new queen not the same as the current then make the new state
            if current_state.pos[queen] != col:

                neighbor_state = current_state.copy()
                neighbor_state.changePos(queen,col)
                neighbor_conflicts = neighbor_state.conflicts()
                # if the number of conflicts of the new state is better take it
                if neighbor_conflicts <= current_conflicts:

                    current_state = neighbor_state
                    current_conflicts = neighbor_conflicts
                    non_improving_counter = 0

                if non_improving_limit > non_improving_counter:
                    non_improving_counter += 1
                else:
                    yield (current_state,f'Local minimum reached conflict is {current_conflicts}') # Local minimum reached
                    return

    yield (current_state,f'no soluton, conflict is {current_conflicts}')

