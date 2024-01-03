### the Nqueen
first, I made the Nqueen class to simplify operations like board making, calculating the conflicts, and displaying.
Note: the solution is that there is only one queen in each diagonal, row, and column
### the algorithms
#### 1. brute-forcing
gives all the solutions possible for the N*N board
by making all the combinations and if a solution is found it appends it

#### 2. Backtracking
Using backtracking it will be faster than brute-forcing,
since it eliminates the solution if a conflict appears.

#### 3. Hillclimbing
it starts with a random state, generates all the next states, and evaluates their conflicts
then it takes the best state found
If the best move does not improve the current state, return it
and terminate if the solution is found or stuck in the Local minimum

#### 4. Hillclimbing Speed
the same as traditional Hillclimbing, but I made the next state to be generated randomly
within n^2 iterations if a better state is found it takes it immediately. 

#### 5. genetic algorithm
using generation and choosing the best solutions then making them produce to make the new population until reaching the solution by lowering the fitness with each generation 
