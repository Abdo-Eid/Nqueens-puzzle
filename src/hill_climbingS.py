from random import randint

# it does one iteration per second almost
def hill_climbing(board, max_iterations=50050,non_improving_limit = 10040):
    # Start with a random initial state
    current_state = board
    n = current_state.n
    current_conflicts = current_state.conflicts()

    non_improving_counter = 0
    for _ in range(max_iterations):
        # If the current state is a solution, return it
        if current_conflicts == 0:
            return current_state

        # another approtch is to get random queen change the pos to random col
        # if there improve select that state
        for _ in range(n^2):
            queen = randint(0,n-1)
            col = randint(0,n-1)
            if current_state.pos[queen] != col:

                neighbor_state = current_state.copy()
                neighbor_state.changePos(queen,col)
                neighbor_conflicts = neighbor_state.conflicts()

                if neighbor_conflicts <= current_conflicts:

                    current_state = neighbor_state
                    current_conflicts = neighbor_conflicts
                    non_improving_counter = 0

                if non_improving_limit > non_improving_counter:
                    non_improving_counter += 1
                else:
                    return None

    return None  # Solution not found within max iterations

