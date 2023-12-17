# it does one iteration per second almost
def hill_climbing(board, max_iterations=10050,non_improving_limit = 600):
    # Start with a random initial state
    current_state = board
    n = current_state.n
    current_conflicts = current_state.conflicts()

    non_improving_counter = 0
    for _ in range(max_iterations):
        # If the current state is a solution, return it
        if current_conflicts == 0:
            return current_state

        # Generate all next states and evaluate their conflicts
        next_states = []
        for queen in range(n): # row since we have only one queen a row
            for col in range(n): # position of the queen on column
                if current_state.pos[queen] != col:
                    neighbor_state = current_state.copy()
                    neighbor_state.changePos(queen,col)
                    next_states.append(neighbor_state)

        next_states_conflicts = [state.conflicts() for state in next_states]
        best_move = next_states[next_states_conflicts.index(min(next_states_conflicts))]

        # If the best move does not improve the current state, return it
        best_conflicts = next_states_conflicts[next_states.index(best_move)]

        if best_conflicts >= current_conflicts:
            non_improving_counter += 1
            if non_improving_counter >= non_improving_limit:
                return current_state  # Local minimum reached
        else:
            non_improving_counter = 0

        # Move to the best state found
        current_state = best_move
        current_conflicts = best_conflicts
    return None  # Solution not found within max iterations